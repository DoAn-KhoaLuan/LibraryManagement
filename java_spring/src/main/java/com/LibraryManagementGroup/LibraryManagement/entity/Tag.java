package com.LibraryManagementGroup.LibraryManagement.entity;

import javax.persistence.Column;


import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Setter
@Getter
@Entity
@Table(name = "tag")
public class Tag {
    @Id
    @GeneratedValue
    @Column(unique = true)
    private Integer id;

    @ManyToMany(mappedBy = "tagList")
    private List<Product> posts = new ArrayList<>();

    @Column(name = "tag_name")
    private String tagName;

    @Column(name = "delete_at")
    private String deteleAt;

    @Column(name = "create_at")
    private String createAt;
}
