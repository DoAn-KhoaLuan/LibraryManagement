package com.LibraryManagementGroup.LibraryManagement.repository;

import com.LibraryManagementGroup.LibraryManagement.entity.District;
import com.LibraryManagementGroup.LibraryManagement.entity.Province;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface DistrictRepository extends JpaRepository<District, Integer> {
}
