package com.LibraryManagementGroup.LibraryManagement.controller;

import com.LibraryManagementGroup.LibraryManagement.common.requests.productrequests.CreateProductRequest;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/admin/order-management")
public class OrderController {
    @PostMapping("/create-order")
    public String createOrder(@RequestBody CreateProductRequest product) {
        return "sadsasa";
    }
}
