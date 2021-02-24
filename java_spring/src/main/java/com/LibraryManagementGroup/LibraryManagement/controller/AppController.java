package com.LibraryManagementGroup.LibraryManagement.controller;

import com.LibraryManagementGroup.LibraryManagement.entity.District;
import com.LibraryManagementGroup.LibraryManagement.entity.Province;
import com.LibraryManagementGroup.LibraryManagement.entity.Ward;
import com.LibraryManagementGroup.LibraryManagement.service.AppService.IAppService;
import com.LibraryManagementGroup.LibraryManagement.service.LocationService.ILocationService;
import net.minidev.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/admin/app-management")
public class AppController {
    @Autowired
    ILocationService locationService;

    @Autowired
    IAppService appService;

    @PostMapping("/load-and-insert-locations")
    public void loadAndInsertLocations(@RequestBody JSONObject req) {
        locationService.loadAndInsertLocations();
    }

    @PostMapping("/get-districts")
    public List<District> getDistricts(@RequestBody JSONObject req) {
        return locationService.getDistricts();
    }

    @PostMapping("/get-provinces")
    public List<Province> getProvinces(@RequestBody JSONObject req) {
        return locationService.getProvinces();
    }

    @PostMapping("/get-wards")
    public List<Ward> getWards(@RequestBody JSONObject req) {
        return locationService.getWards();
    }

    @PostMapping("/test")
    public String test(@RequestBody JSONObject req) {
        return "TEST";
    }



}
