package com.LibraryManagementGroup.LibraryManagement.common.response.accountresponses;

import com.LibraryManagementGroup.LibraryManagement.entity.Account;
import lombok.*;

@Getter
@Setter
public class RegisterShopResponse {
    private Integer id;
    private String shopName;
    private String websiteUrl;
    private String imageUrl;
    private String provinceId;
    private String districtId;
    private String wardId;
    private String deteleAt;
    private String createAt;
    private RegisterAccountResponse account;
}
