package com.LibraryManagementGroup.LibraryManagement.entity;

import javax.persistence.*;
import java.util.Date;
import java.util.List;

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
