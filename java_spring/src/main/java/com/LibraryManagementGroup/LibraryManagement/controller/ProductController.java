package com.LibraryManagementGroup.LibraryManagement.controller;

import com.LibraryManagementGroup.LibraryManagement.entity.Province;
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
@RequestMapping("/admin")
public class ProductController {
    @Autowired
    ProvinceRepository provinceRep;

    @PostMapping("/loadProvinces")
    public JSONObject createBook(@RequestBody JSONObject reqq) {
//        final  String getProvincesURI = "https://shop.d.etop.vn/api/etop.Location/GetProvinces";
//        final  String getDistrictsURI = "https://shop.d.etop.vn/api/etop.Location/GetDistricts";
//        final  String getWardsURI = "https://shop.d.etop.vn/api/etop.Location/GetWards";
//        RestTemplate restTemplate = new RestTemplate();
        JSONObject req = new JSONObject();
        req.put("ádasdsa", "Dsadsa");
//        JSONObject provincesRes = restTemplate.postForObject(getProvincesURI, req, JSONObject.class);
//        JSONObject districtsRes = restTemplate.postForObject(getDistrictsURI, req, JSONObject.class);
//        JSONObject wardsRes = restTemplate.postForObject(getWardsURI, req, JSONObject.class);
//        List<LinkedHashMap> provinceList= (ArrayList) provincesRes.get("provinces");
//        for (LinkedHashMap province: provinceList) {
//            Province prov = new Province();
//            prov.setId((String)province.get("code"));
////			prov.setName((String)province.get("name"));
////			prov.setRegion((String)province.get("region"));
//            System.out.println((String)province.get("code"));
//            System.out.println((String)province.get("name"));
//            System.out.println((String)province.get("region"));
//            Integer res = provinceRep.insertProvince((String)province.get("code"),(String)province.get("name"), (String)province.get("region"));
//        };
        return req;
    }
}
