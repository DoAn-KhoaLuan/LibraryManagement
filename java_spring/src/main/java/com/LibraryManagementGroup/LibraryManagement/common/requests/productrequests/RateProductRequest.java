package com.LibraryManagementGroup.LibraryManagement.common.requests.productrequests;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class RateProductRequest {
    private int productId;
    private float productStar;
}
