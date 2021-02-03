package com.LibraryManagementGroup.LibraryManagement.repository;

import com.LibraryManagementGroup.LibraryManagement.entity.Ward;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface WardRepository extends JpaRepository<Ward, Integer> {
}
