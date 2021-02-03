package com.LibraryManagementGroup.LibraryManagement.repository;

import com.LibraryManagementGroup.LibraryManagement.entity.Province;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import javax.transaction.Transactional;

@Repository
public interface ProvinceRepository extends JpaRepository<Province, String> {
    @Modifying
    @Transactional
    @Query(nativeQuery = true, value = "insert into province value (?1, ?2, ?3)")
    int insertProvince(String id, String name, String region);
}
