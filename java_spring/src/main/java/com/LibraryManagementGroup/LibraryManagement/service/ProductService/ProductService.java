package com.LibraryManagementGroup.LibraryManagement.service.ProductService;

import com.LibraryManagementGroup.LibraryManagement.common.dto.ProductDto;
import com.LibraryManagementGroup.LibraryManagement.common.requests.commons.GetItemRequest;
import com.LibraryManagementGroup.LibraryManagement.common.requests.productrequests.*;
import com.LibraryManagementGroup.LibraryManagement.common.response.accountresponses.RegisterAccountResponse;
import com.LibraryManagementGroup.LibraryManagement.entity.*;
import com.LibraryManagementGroup.LibraryManagement.repository.*;
import net.minidev.json.JSONObject;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
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

    @Autowired
    TagRepository tagRepository;

    @Override
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

        String[] tags = prod.getTags();
        for (String tag: tags) {
            Tag tagEnt = new Tag();
            tagEnt.setTagName(tag);
            tagEnt.setCreateAt(new Date().toString());
            tagEnt.addProducts(createdProduct);
        }
        productRepository.save(createdProduct);
        return prod;
    }

    @Override
    public Integer deleteProduct(DeteleProductRequest req) {
        return productRepository.deleteProduct(req.getId(), new Date().toString());
    }

    @Override
    public Product getProduct(GetItemRequest req) {
        return productRepository.getOne(req.getId());
    }

    @Override
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

    @Override
    public CreateTagRequest createTag(CreateTagRequest tag) {
        Tag createTag = new Tag();
        createTag.setTagName(tag.getTagName());
        tagRepository.save(createTag);
        return tag;
    }

    @Override
    public List<ProductDto> getProductsByShopId(int shopId) {
        ModelMapper modelMapper = new ModelMapper();
        List<Product> entityProducts = productRepository.getProductsByShopId(shopId);
        List<ProductDto> dtoProducts = new ArrayList<>();
        for (Product entityProduct:entityProducts) {
            ProductDto productDto = modelMapper.map(entityProduct, ProductDto.class);
            dtoProducts.add(productDto);
        }
        return dtoProducts;
    }

    @Override
    public ProductDto rateProduct(RateProductRequest req) {
        ModelMapper modelMapper = new ModelMapper();
        System.out.println("product" + req.getProductId());
        Product product = productRepository.getOne(req.getProductId());
        float newStar = ((product.getRateStart() * product.getRateCount()) + req.getProductStar()) / (product.getRateCount() + 1);
        product.setRateStart(newStar);
        product.setRateCount(product.getRateCount() + 1);
        productRepository.save(product);
        ProductDto dtoProduct = modelMapper.map(product,ProductDto.class);
        return dtoProduct;
    }
}
