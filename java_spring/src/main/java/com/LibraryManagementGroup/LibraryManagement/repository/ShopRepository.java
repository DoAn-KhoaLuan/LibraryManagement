package com.LibraryManagementGroup.LibraryManagement.repository;


import com.LibraryManagementGroup.LibraryManagement.entity.Shop;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ShopRepository extends JpaRepository<Shop, Integer> {
}
