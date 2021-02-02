package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.Date;
import java.util.List;
@Setter
@Getter
@Entity
@Table(name="role")
public class Role {
    @Id
    @GeneratedValue
    private int id;

    @OneToMany(mappedBy = "role",cascade = CascadeType.ALL)
    private List<Account> accounts;

    private String role_name;

    private String note;

    private Date deleted_at;
}
