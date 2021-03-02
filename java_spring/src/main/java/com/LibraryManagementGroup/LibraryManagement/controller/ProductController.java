package com.LibraryManagementGroup.LibraryManagement.controller;

import com.LibraryManagementGroup.LibraryManagement.common.requests.productrequests.CreateProductRequest;
import com.LibraryManagementGroup.LibraryManagement.common.requests.productrequests.DeteleProductRequest;
import com.LibraryManagementGroup.LibraryManagement.common.requests.productrequests.UpdateProductRequest;
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

    @PostMapping("/update-product")
    public UpdateProductRequest updateProduct(@RequestBody UpdateProductRequest req) {
        return productService.updateProduct(req);
    }
}
