package com.LibraryManagementGroup.LibraryManagement.service.ProductService;

import com.LibraryManagementGroup.LibraryManagement.common.requests.productrequests.CreateProductRequest;
import com.LibraryManagementGroup.LibraryManagement.common.requests.productrequests.DeteleProductRequest;
import com.LibraryManagementGroup.LibraryManagement.common.requests.productrequests.UpdateProductRequest;
import com.LibraryManagementGroup.LibraryManagement.common.response.accountresponses.RegisterAccountResponse;
import com.LibraryManagementGroup.LibraryManagement.entity.Account;
import com.LibraryManagementGroup.LibraryManagement.entity.Category;
import com.LibraryManagementGroup.LibraryManagement.entity.Product;
import com.LibraryManagementGroup.LibraryManagement.entity.Shop;
import com.LibraryManagementGroup.LibraryManagement.entity.Supplier;
import com.LibraryManagementGroup.LibraryManagement.repository.CategoryRepository;
import com.LibraryManagementGroup.LibraryManagement.repository.ProductRepository;
import com.LibraryManagementGroup.LibraryManagement.repository.ShopRepository;
import com.LibraryManagementGroup.LibraryManagement.repository.SupplierRepository;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.Optional;


@Service
public class ProductService implements IProductService {
    @Autowired
    ProductRepository productRepository;

    @Autowired
    ShopRepository shopRepository;

    @Autowired
    CategoryRepository categoryRepository;

    @Autowired
    SupplierRepository supplierRepository;

    public CreateProductRequest createProduct(CreateProductRequest prod) {

        Product createdProduct = new Product();
        createdProduct.setCreateAt(new Date().toString());
        createdProduct.setAmount(prod.getAmount());
        createdProduct.setBrandName(prod.getBrandName());
        createdProduct.setMaterial(prod.getMaterial());
        createdProduct.setOrigin(prod.getOrigin());
        createdProduct.setCostPrice(prod.getCostPrice());
        createdProduct.setRetailPrice(prod.getRetailPrice());
        createdProduct.setDescription(prod.getDescription());
        createdProduct.setImageUrl(prod.getImageUrl());
        createdProduct.setFeature(prod.getFeature());
        createdProduct.setDiscount(prod.getDiscount());
        createdProduct.setSize(prod.getSize());
        createdProduct.setProductName(prod.getProductName());

        Shop productShop = shopRepository.getOne(prod.getShopId());
        createdProduct.setShop(productShop);
//
        Category productCategory = categoryRepository.getOne(prod.getCategoryId());
        createdProduct.setCategory(productCategory);

        Supplier productSupplier = supplierRepository.getOne(prod.getSupplierId());
        createdProduct.setSupplier(productSupplier);

        productRepository.save(createdProduct);
        return prod;
    }

    public Integer deleteProduct(DeteleProductRequest req) {
        return productRepository.deleteProduct(req.getId(), new Date().toString());
    }

    public UpdateProductRequest updateProduct(UpdateProductRequest prod) {
        Product updateProduct = productRepository.getOne(prod.getId());
        if (prod.getAmount() != null) {
            updateProduct.setAmount(prod.getAmount());
        }

        if (prod.getBrandName() != null) {
            updateProduct.setBrandName(prod.getBrandName());
        }

        if (prod.getMaterial() != null) {
            updateProduct.setMaterial(prod.getMaterial());
        }

        if (prod.getOrigin() != null) {
            updateProduct.setOrigin(prod.getOrigin());

        }

        if (prod.getCostPrice() > 0) {
            updateProduct.setCostPrice(prod.getCostPrice());
        }

        if (prod.getRetailPrice() > 0) {
            updateProduct.setRetailPrice(prod.getRetailPrice());

        }

        if (prod.getDescription() != null) {
            updateProduct.setDescription(prod.getDescription());

        }

        if (prod.getImageUrl() != null) {
            updateProduct.setImageUrl(prod.getImageUrl());
        }

        if (prod.getFeature() != null) {
            updateProduct.setFeature(prod.getFeature());
        }

        if (prod.getDiscount() > 0) {
            updateProduct.setDiscount(prod.getDiscount());
        }

        if (prod.getSize() != null) {
            updateProduct.setSize(prod.getSize());
        }

        if (prod.getProductName() != null) {
            updateProduct.setProductName(prod.getProductName());
        }

        productRepository.saveAndFlush(updateProduct);
        return prod;
    }

}
