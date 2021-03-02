package com.LibraryManagementGroup.LibraryManagement.repository;

import com.LibraryManagementGroup.LibraryManagement.entity.Category;
import com.LibraryManagementGroup.LibraryManagement.entity.Supplier;
import com.LibraryManagementGroup.LibraryManagement.entity.Ward;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface SupplierRepository extends JpaRepository<Supplier, Integer> {

//    @Query("select s from Supplier s where id =?1")
//    Supplier getOne(int id);
}
