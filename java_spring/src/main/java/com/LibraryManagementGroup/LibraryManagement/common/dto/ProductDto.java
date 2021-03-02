package com.LibraryManagementGroup.LibraryManagement.common.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ProductDto {
    private String productName;
    private Integer amount;
    private String imageUrl;
    private String description;
    private String brandName;
    private String feature;
    private String material;
    private String origin;
    private String size;
    private float costPrice;
    private float retailPrice;
    private float discount;
    private Integer shopId;
    private Integer categoryId;
    private Integer supplierId;
    private String[] tags;
}
