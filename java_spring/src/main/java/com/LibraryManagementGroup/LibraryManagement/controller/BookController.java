package com.LibraryManagementGroup.LibraryManagement.controller;

import org.springframework.web.bind.annotation.*;

@RestController
public class BookController {

    @GetMapping("/get-books")
    public Integer getBooks() {
        return 1;
    }
}