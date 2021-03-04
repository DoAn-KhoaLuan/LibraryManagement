package com.LibraryManagementGroup.LibraryManagement.entity;

import javax.persistence.Column;

import javax.persistence.*;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Setter
@Getter
@Entity
@Table(name = "category")
public class Category {
//    public Category(String categoryName, String description, String note, String createAt) {
//        this.categoryName = categoryName;
//        this.description = description;
//        this.note = note;
//        this.createAt = createAt;
//    }

    @Id
    @GeneratedValue
    @Column(unique = true)
    private Integer id;

    @Column(name = "category_name", unique=true)
    private String categoryName;

    @OneToMany(fetch = FetchType.LAZY, mappedBy = "category")
    private Set<Product> products  = new HashSet<>();

    @Column(name = "description")
    private String description;

    @Column(name = "note")
    private String note;

    @Column(name = "delete_at")
    private String deteleAt;

    @Override
    public String toString() {
        return "Category{" +
                "id=" + id +
                ", productList=" + products +
                ", categoryName='" + categoryName + '\'' +
                ", description='" + description + '\'' +
                ", note='" + note + '\'' +
                ", deteleAt='" + deteleAt + '\'' +
                ", createAt='" + createAt + '\'' +
                '}';
    }

    @Column(name = "create_at")
    private String createAt;
}
