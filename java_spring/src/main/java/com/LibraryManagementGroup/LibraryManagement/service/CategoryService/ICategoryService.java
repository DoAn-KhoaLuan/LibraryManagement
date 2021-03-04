package com.LibraryManagementGroup.LibraryManagement.service.CategoryService;

import com.LibraryManagementGroup.LibraryManagement.common.dto.CategoryDto;
import com.LibraryManagementGroup.LibraryManagement.entity.Category;

import java.util.List;

public interface ICategoryService {
    public List<CategoryDto> getAllCategories();
    public void insertCategories();
}
