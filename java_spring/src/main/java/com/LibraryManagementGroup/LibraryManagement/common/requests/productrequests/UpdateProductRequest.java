package com.LibraryManagementGroup.LibraryManagement.common.requests.productrequests;

import com.LibraryManagementGroup.LibraryManagement.common.dto.ProductDto;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class UpdateProductRequest extends ProductDto {
    private Integer id;
}
