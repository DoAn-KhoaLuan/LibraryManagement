package com.LibraryManagementGroup.LibraryManagement.service.ProductService;

import com.LibraryManagementGroup.LibraryManagement.common.dto.ProductDto;
import com.LibraryManagementGroup.LibraryManagement.common.requests.commons.GetItemRequest;
import com.LibraryManagementGroup.LibraryManagement.common.requests.productrequests.*;
import com.LibraryManagementGroup.LibraryManagement.entity.Product;
import net.minidev.json.JSONObject;

import java.util.List;

public interface IProductService {
    public CreateProductRequest createProduct(CreateProductRequest prod);
    public Integer deleteProduct(DeteleProductRequest req);
    public UpdateProductRequest updateProduct(UpdateProductRequest prod);
    public List<ProductDto>  getProductsByShopId(int shopId);
    public CreateTagRequest createTag(CreateTagRequest tag);
    public ProductDto rateProduct(RateProductRequest req);
    public Product getProduct(GetItemRequest req);
}
