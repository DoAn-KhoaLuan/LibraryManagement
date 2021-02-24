package com.LibraryManagementGroup.LibraryManagement.common.response.accountresponses;

import com.LibraryManagementGroup.LibraryManagement.entity.Shop;

public class LoginResponse {
    private String accessToken;
    private RegisterAccountResponse account;
//    private Shop shop;

    @Override
    public String toString() {
        return "LoginResponse{" +
                "accessToken='" + accessToken + '\'' +
                ", account=" + account +
//                ", shop=" + shop +
                '}';
    }

//    public LoginResponse(String accessToken, RegisterAccountResponse account, Shop shop) {
//        this.accessToken = accessToken;
//        this.account = account;
//        this.shop = shop;
//    }

    public LoginResponse(String accessToken, RegisterAccountResponse account) {
        this.accessToken = accessToken;
        this.account = account;
    }

//    public LoginResponse(String accessToken) {
//        this.accessToken = accessToken;
//    }

}
