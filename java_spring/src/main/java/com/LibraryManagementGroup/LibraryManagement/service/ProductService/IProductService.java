package com.LibraryManagementGroup.LibraryManagement.service.ProductService;

import com.LibraryManagementGroup.LibraryManagement.common.requests.productrequests.CreateProductRequest;
import com.LibraryManagementGroup.LibraryManagement.entity.Product;

public interface IProductService {
    public CreateProductRequest createProduct(CreateProductRequest prod);
}
