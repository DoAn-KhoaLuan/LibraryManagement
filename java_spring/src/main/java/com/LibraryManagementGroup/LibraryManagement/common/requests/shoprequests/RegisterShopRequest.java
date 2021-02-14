package com.LibraryManagementGroup.LibraryManagement.common.requests.shoprequests;

import lombok.*;

@Getter
@Setter
public class RegisterShopRequest {
    private String shopName;
    private String websiteUrl;
    private String imageUrl;
    private String provinceId;
    private String districtId;
    private String wardId;
    private Integer accountId;

}
