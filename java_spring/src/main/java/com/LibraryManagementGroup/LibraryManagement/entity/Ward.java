package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

@Setter
@Getter
@Entity
@Table(name = "ward")
public class Ward {
    @Id
    @Column(unique = true)
    private String id;

    @Column(name = "name")
    private String name;

    @Column(name = "district_id")
    private String districtId;

}
