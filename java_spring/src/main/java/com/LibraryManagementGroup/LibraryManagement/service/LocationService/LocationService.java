package com.LibraryManagementGroup.LibraryManagement.service.LocationService;

import com.LibraryManagementGroup.LibraryManagement.entity.District;
import com.LibraryManagementGroup.LibraryManagement.entity.Province;
import com.LibraryManagementGroup.LibraryManagement.entity.Ward;
import com.LibraryManagementGroup.LibraryManagement.repository.DistrictRepository;
import com.LibraryManagementGroup.LibraryManagement.repository.ProvinceRepository;
import com.LibraryManagementGroup.LibraryManagement.repository.WardRepository;
import net.minidev.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;

@Service
public class LocationService implements ILocationService {
    @Autowired
    ProvinceRepository provinceRepository;

    @Autowired
    DistrictRepository districtRepository;

    @Autowired
    WardRepository wardRepository;

    @Override
    public List<Ward> getWards() {
        return wardRepository.findAll();
    }

    @Override
    public List<District> getDistricts() {
        return districtRepository.findAll();
    }

    @Override
    public List<Province> getProvinces() {
        return provinceRepository.findAll();
    }

    @Override
    public void loadAndInsertLocations() {
        JSONObject obj = new JSONObject();
        final  String getProvincesURI = "https://shop.d.etop.vn/api/etop.Location/GetProvinces";
        final  String getDistrictsURI = "https://shop.d.etop.vn/api/etop.Location/GetDistricts";
        final  String getWardsURI = "https://shop.d.etop.vn/api/etop.Location/GetWards";
        RestTemplate restTemplate = new RestTemplate();

        JSONObject provincesRes = restTemplate.postForObject(getProvincesURI, obj, JSONObject.class);
        JSONObject districtsRes = restTemplate.postForObject(getDistrictsURI, obj, JSONObject.class);
        JSONObject wardsRes = restTemplate.postForObject(getWardsURI, obj, JSONObject.class);

        List<LinkedHashMap> provinceList= (ArrayList) provincesRes.get("provinces");
        List<LinkedHashMap> districtList= (ArrayList) districtsRes.get("districts");
        List<LinkedHashMap> wardList= (ArrayList) wardsRes.get("wards");

        for(LinkedHashMap province: provinceList) {
            Province provinceEntity = new Province();
            provinceEntity.setId((String) province.get("code"));
            provinceEntity.setName((String) province.get("name"));
            provinceEntity.setRegion((String) province.get("region"));
            provinceRepository.save(provinceEntity);
        }

        for(LinkedHashMap district: districtList) {
            District districtEntity = new District();
            districtEntity.setId((String) district.get("code"));
            districtEntity.setName((String) district.get("name"));
            districtEntity.setProvinceId((String) district.get("province_code"));
            districtRepository.save(districtEntity);
        }

        for(LinkedHashMap ward: wardList) {
            Ward wardEntity = new Ward();
            wardEntity.setId((String) ward.get("code"));
            wardEntity.setName((String) ward.get("name"));
            wardEntity.setDistrictId((String) ward.get("district_code"));
            wardRepository.save(wardEntity);
        }
    }
}
