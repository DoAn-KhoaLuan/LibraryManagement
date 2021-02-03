package com.LibraryManagementGroup.LibraryManagement.service.LocationService;

import com.LibraryManagementGroup.LibraryManagement.entity.District;
import com.LibraryManagementGroup.LibraryManagement.entity.Province;
import com.LibraryManagementGroup.LibraryManagement.entity.Ward;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface ILocationService {
    public void loadAndInsertLocations();
//    public List<District> getDistricts();
    public List<Province> getProvinces();
    public List<Ward> getWards();
    public List<District> getDistricts();
}
