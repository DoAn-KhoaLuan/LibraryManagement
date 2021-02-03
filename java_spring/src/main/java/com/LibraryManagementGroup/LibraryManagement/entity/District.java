package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

@Setter
@Getter
@Entity
@Table(name = "district")
public class District {
    @Id
    @Column(name="id",unique = true)
    private String id;

    @Column(name = "province_id")
    private String provinceId;

    @Column(name = "name")
    private String name;
}
