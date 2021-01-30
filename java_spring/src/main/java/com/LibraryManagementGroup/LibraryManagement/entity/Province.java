package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.List;
@Setter
@Getter
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
