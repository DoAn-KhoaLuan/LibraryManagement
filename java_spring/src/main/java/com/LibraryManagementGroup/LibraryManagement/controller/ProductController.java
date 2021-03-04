package com.LibraryManagementGroup.LibraryManagement.controller;

import com.LibraryManagementGroup.LibraryManagement.common.dto.ProductDto;
import com.LibraryManagementGroup.LibraryManagement.common.requests.commons.GetItemRequest;
import com.LibraryManagementGroup.LibraryManagement.common.requests.productrequests.*;
import com.LibraryManagementGroup.LibraryManagement.entity.Product;
import com.LibraryManagementGroup.LibraryManagement.service.CategoryService.CategoryService;
import com.LibraryManagementGroup.LibraryManagement.service.ProductService.ProductService;
import net.minidev.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Date;
import java.util.List;

@RestController
@RequestMapping("/admin/product-management")
public class ProductController {
    @Autowired
    ProductService productService;

    @PostMapping("/create-product")
    public CreateProductRequest createProduct(@RequestBody CreateProductRequest product) {
        return productService.createProduct(product);
    }

    @PostMapping("/delete-product")
    public Integer createProduct(@RequestBody DeteleProductRequest req) {
        return productService.deleteProduct(req);
    }

    @PostMapping("/get-product")
    public Product getProduct(@RequestBody GetItemRequest req) {
        return productService.getProduct(req);
    }

    @PostMapping("/update-product")
    public UpdateProductRequest updateProduct(@RequestBody UpdateProductRequest req) {
        return productService.updateProduct(req);
    }

    @PostMapping("/create-tag")
    public CreateTagRequest createTag(@RequestBody CreateTagRequest req) {
        return productService.createTag(req);
    }

    @PostMapping("/get-shop-products")
    public JSONObject getShopProducts(@RequestBody JSONObject req) {
        JSONObject res = new JSONObject();
        List<ProductDto> products = productService.getProductsByShopId(18);
        res.put("products", products);
        return res;
    }

    @PostMapping("/rate-product")
    public ProductDto rateProduct(@RequestBody RateProductRequest req) {
        return productService.rateProduct(req);
    }
}
