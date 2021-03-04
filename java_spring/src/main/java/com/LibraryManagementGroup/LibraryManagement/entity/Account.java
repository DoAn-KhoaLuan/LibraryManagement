package com.LibraryManagementGroup.LibraryManagement.entity;
import lombok.Getter;
import lombok.Setter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

import javax.persistence.*;
import java.util.Date;
import java.util.HashSet;
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
    private Set<Comment> comments = new HashSet<>();;

    @OneToMany(mappedBy = "customerAccount")
    private Set<Order> buyOrders = new HashSet<>();;

    @OneToMany(mappedBy = "shopAccount")
    private Set<Order> sellOrders = new HashSet<>();;

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

    @Column(name = "account_name", unique = true)
    private String accountName;

    @Column(name = "account_password")
    private String accountPassword;

    @Column(name = "last_name")
    private String lastName;

    @Column(name = "first_name")
    private String firstName;

    @Column(name = "phone")
    private String phone;

    @Column(name = "email")
    private String email;

    @Column(name = "birth_date")
    private Date birthDate;

    @Column(name = "image_url", length = 1000)
    private String imageUrl;

    @Column(name = "note", length = 1000)
    private String note;

    @Column(name = "delete_at")
    private String deteleAt;

    @Column(name = "create_at")
    private String createAt;

    @Override
    public String toString() {
        return String.format(accountName + " + i" + accountName);
    }

    public void encodePassword() {
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder(16);
        String encodedPassword = passwordEncoder.encode(this.getAccountPassword());
        this.setAccountPassword(encodedPassword);
    }
}
