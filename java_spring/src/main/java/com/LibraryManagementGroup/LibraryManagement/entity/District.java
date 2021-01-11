package com.LibraryManagementGroup.LibraryManagement.entity;

import javax.persistence.*;
import java.util.List;
import java.util.Properties;

@Entity
@Table(name="district")
public class District {
    @Id
    @GeneratedValue
    private int id;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "province_id")
    private Province province;

    @OneToMany(mappedBy = "district")
    private List<Ward> wards;

    private String name;
}
