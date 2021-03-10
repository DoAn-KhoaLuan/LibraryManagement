package com.LibraryManagementGroup.LibraryManagement.repository;

import com.LibraryManagementGroup.LibraryManagement.entity.Order;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OrderRepository extends JpaRepository<Order, Integer> {
}
