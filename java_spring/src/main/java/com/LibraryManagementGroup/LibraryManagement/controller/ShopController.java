package com.LibraryManagementGroup.LibraryManagement.controller;

import com.LibraryManagementGroup.LibraryManagement.common.requests.shoprequests.RegisterShopRequest;
import com.LibraryManagementGroup.LibraryManagement.common.response.accountresponses.RegisterAccountResponse;
import com.LibraryManagementGroup.LibraryManagement.common.response.accountresponses.RegisterShopResponse;
import com.LibraryManagementGroup.LibraryManagement.entity.Account;
import com.LibraryManagementGroup.LibraryManagement.entity.Shop;
import com.LibraryManagementGroup.LibraryManagement.service.ShopService.ShopService;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/admin/shop-management")
public class ShopController {
    @Autowired
    ShopService shopService;

    @PostMapping("/register")
    public ResponseEntity<?> registerShop(@RequestBody RegisterShopRequest shopReq) {
        try {
            ModelMapper modelMapper = new ModelMapper();
            Shop registerShop = shopService.registerShop(shopReq);

            RegisterShopResponse res = modelMapper.map(registerShop, RegisterShopResponse.class);
            return ResponseEntity.ok(res);
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.badRequest().body(e.getMessage());
        }

    }
}
