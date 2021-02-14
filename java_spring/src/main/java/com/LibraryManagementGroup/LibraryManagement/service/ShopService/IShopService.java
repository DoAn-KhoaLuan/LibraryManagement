package com.LibraryManagementGroup.LibraryManagement.service.ShopService;

import com.LibraryManagementGroup.LibraryManagement.common.requests.shoprequests.RegisterShopRequest;
import com.LibraryManagementGroup.LibraryManagement.entity.Shop;

public interface IShopService {
    public Shop registerShop(RegisterShopRequest shopReq);
}
