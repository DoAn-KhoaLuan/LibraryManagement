package com.LibraryManagementGroup.LibraryManagement.service.CategoryService;

import com.LibraryManagementGroup.LibraryManagement.entity.Category;

import java.util.List;

public interface ICategoryService {
    public List<Category> getAllCategories();
    public void insertCategories();
}
