package com.LibraryManagementGroup.LibraryManagement.entity;

import javax.persistence.*;
import java.util.List;

@Entity
@Table(name = "province")
public class Province {
    @Id
    @GeneratedValue
    private int id;

    @OneToMany(mappedBy = "province")
    private List<District> districts;

    private String  name;
    private String  region;

}
