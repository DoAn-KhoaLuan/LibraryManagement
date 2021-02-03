package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Setter
@Getter
@Entity
@Table(name = "ward")
public class Ward {
    @Id
    @Column(unique = true)
    private String id;

    @Column(name = "district_id")
    private String districtId;

    @Column(name = "name")
    private String name;
}
