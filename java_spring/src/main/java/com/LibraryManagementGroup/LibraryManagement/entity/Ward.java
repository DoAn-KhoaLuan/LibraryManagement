package com.LibraryManagementGroup.LibraryManagement.entity;

import javax.persistence.*;

@Entity
@Table(name="ward")
public class Ward {
    @Id
    @GeneratedValue
    private int id;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "district_id")
    private District district;

    private String name;
}
