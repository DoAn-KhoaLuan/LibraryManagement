package com.LibraryManagementGroup.LibraryManagement.controller;

import com.LibraryManagementGroup.LibraryManagement.entity.District;
import com.LibraryManagementGroup.LibraryManagement.entity.Province;
import com.LibraryManagementGroup.LibraryManagement.entity.Ward;
import com.LibraryManagementGroup.LibraryManagement.repository.ProvinceRepository;
import net.minidev.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;

@RestController
@RequestMapping("/admin/author-management")
public class AuthorController {
    @Autowired ProvinceRepository provinceRepository;

    @PostMapping("/loadProvinces")
    public Integer loadProvices(@RequestBody JSONObject req) {
        final  String getProvincesURI = "https://shop.d.etop.vn/api/etop.Location/GetProvinces";
        final  String getDistrictsURI = "https://shop.d.etop.vn/api/etop.Location/GetDistricts";
        final  String getWardsURI = "https://shop.d.etop.vn/api/etop.Location/GetWards";
        RestTemplate restTemplate = new RestTemplate();
        JSONObject provincesRes = restTemplate.postForObject(getProvincesURI, req, JSONObject.class);
        JSONObject districtsRes = restTemplate.postForObject(getDistrictsURI, req, JSONObject.class);
        JSONObject wardsRes = restTemplate.postForObject(getWardsURI, req, JSONObject.class);
        List<LinkedHashMap> provinceList= (ArrayList) provincesRes.get("provinces");
        List<LinkedHashMap> districtList= (ArrayList) districtsRes.get("districts");
        List<LinkedHashMap> wardList= (ArrayList) wardsRes.get("wards");

        for(LinkedHashMap province: provinceList) {
            Province provinceEntity = new Province();
            provinceEntity.setId((String) province.get("code"));
            provinceEntity.setName((String) province.get("name"));
            provinceEntity.setRegion((String) province.get("region"));
            for(LinkedHashMap district: districtList) {
                District districtEntity = new District();
                if (district.get("province_code").equals(province.get("code"))) {
                    System.out.println("BANG NHAU NAA");
                    districtEntity.setId((String) district.get("code"));
                    districtEntity.setName((String) district.get("name"));
                }
                for(LinkedHashMap ward: wardList) {
                    Ward wardEntity = new Ward();
                    if (ward.get("district_code").equals(district.get("code"))) {
                        wardEntity.setId((String) ward.get("code"));
                        wardEntity.setName((String) ward.get("name"));
                    }
                }
            }
            provinceRepository.save(provinceEntity);
        }
        return 1;
    }
}
