package com.LibraryManagementGroup.LibraryManagement.entity;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.Date;
import java.util.Set;

@Setter
@Getter
@Entity
@Table(name = "account")
public class Account {
    @Id
    @GeneratedValue
    @Column(unique = true)
    private Integer id;

    @OneToMany(mappedBy = "account")
    private Set<Comment> commentList;

    @OneToMany(mappedBy = "customerAccount")
    private Set<Order> BuyOrderList;

    @OneToMany(mappedBy = "shopAccount")
    private Set<Order> SellOrderList;

    @Column(name = "province_id")
    private String provinceId;

    @Column(name = "district_id")
    private String districtId;

    @Column(name = "ward_id")
    private String wardId;

    @Column(name = "address")
    private String address;

    @Column(name = "role_name")
    private RoleName roleName;

    @Column(name = "account_name")
    private String accountName;

    @Column(name = "account_password")
    private String account_password;

    @Column(name = "last_name")
    private String last_name;

    @Column(name = "first_name")
    private String first_name;

    @Column(name = "phone")
    private String phone;

    @Column(name = "email")
    private String email;

    @Column(name = "birth_date")
    private Date birthdate;

    @Column(name = "image_url", length = 1000)
    private String image_url;

    @Column(name = "note", length = 1000)
    private String note;

    @Column(name = "delete_at")
    private String deteleAt;

    @Column(name = "create_at")
    private String createAt;
}
