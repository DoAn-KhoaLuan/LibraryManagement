package com.LibraryManagementGroup.LibraryManagement.service.ShopService;

import com.LibraryManagementGroup.LibraryManagement.common.requests.shoprequests.RegisterShopRequest;
import com.LibraryManagementGroup.LibraryManagement.entity.Account;
import com.LibraryManagementGroup.LibraryManagement.entity.Shop;
import com.LibraryManagementGroup.LibraryManagement.repository.AccountRepository;
import com.LibraryManagementGroup.LibraryManagement.repository.ShopRepository;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.Optional;

@Service
public class ShopService implements IShopService{
    @Autowired
    ShopRepository shopRepository;

    @Autowired
    AccountRepository accountRepository;

    @Override
    public Shop registerShop(RegisterShopRequest shopReq) {
        Account shopAccount = accountRepository.getAccountById(shopReq.getAccountId());
        Date createAt = new Date();
        String shopName = shopReq.getShopName();
        String websiteUrl = shopReq.getWebsiteUrl();
        String imageUrl = shopReq.getImageUrl();
        String provinceId = shopReq.getProvinceId();
        String districtId = shopReq.getDistrictId();
        String wardId = shopReq.getWardId();

        Shop registerShopEntity = new Shop();
        registerShopEntity.setCreateAt(createAt.toString());
        registerShopEntity.setAccount(shopAccount);
        registerShopEntity.setShopName(shopName);
        registerShopEntity.setWebsiteUrl(websiteUrl);
        registerShopEntity.setImageUrl(imageUrl);
        registerShopEntity.setProvinceId(provinceId);
        registerShopEntity.setDistrictId(districtId);
        registerShopEntity.setWardId(wardId);

        return shopRepository.saveAndFlush(registerShopEntity);
    }
}
