package com.LibraryManagementGroup.LibraryManagement.controller;

import com.LibraryManagementGroup.LibraryManagement.entity.Category;
import com.LibraryManagementGroup.LibraryManagement.repository.CategoryRepository;
import com.LibraryManagementGroup.LibraryManagement.service.AppService.IAppService;
import com.LibraryManagementGroup.LibraryManagement.service.CategoryService.CategoryService;
import com.LibraryManagementGroup.LibraryManagement.service.CategoryService.ICategoryService;
import com.LibraryManagementGroup.LibraryManagement.service.LocationService.LocationService;
import net.minidev.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/admin/category-management")
public class CategoryController {
    @Autowired
    IAppService appService;

    @Autowired
    LocationService locationService;

    @Autowired
    CategoryService categoryService;

    @PostMapping("/init-categories")
    public boolean insertCategories(@RequestBody JSONObject req) {
        categoryService.insertCategories();
        return true;
    }

    @PostMapping("/get-categories")
    public ResponseEntity<?> getCategories(@RequestBody JSONObject req) {
        JSONObject res = new JSONObject();
        res.put("categories", categoryService.getAllCategories());
        return ResponseEntity.ok(res);
    }
}
