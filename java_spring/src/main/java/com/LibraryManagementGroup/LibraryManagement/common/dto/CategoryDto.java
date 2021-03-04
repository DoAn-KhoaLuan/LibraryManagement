package com.LibraryManagementGroup.LibraryManagement.common.dto;

import com.LibraryManagementGroup.LibraryManagement.entity.Product;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Getter
@Setter
public class CategoryDto {

    private Integer id;

    private String categoryName;


    private String description;

    private String note;

    private String deteleAt;
}
