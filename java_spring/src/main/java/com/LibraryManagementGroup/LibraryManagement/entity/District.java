package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;

@Setter
@Getter
@Entity
@Table(name = "district")
public class District {
    @Id
    @Column(name="id",unique = true)
    private String id;

    @Column(name = "name")
    private String name;

    @Column(name = "province_id")
    private String provinceId;
}
