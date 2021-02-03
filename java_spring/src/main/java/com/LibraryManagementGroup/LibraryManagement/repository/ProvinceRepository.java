package com.LibraryManagementGroup.LibraryManagement.repository;

import com.LibraryManagementGroup.LibraryManagement.entity.District;
import com.LibraryManagementGroup.LibraryManagement.entity.Province;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import javax.transaction.Transactional;
import java.util.List;

@Repository
public interface ProvinceRepository extends JpaRepository<Province, Integer> {
}
