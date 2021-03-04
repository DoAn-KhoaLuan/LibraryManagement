package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Setter
@Getter
@Entity
@Table(name="shop")
public class Shop {
    @Id
    @GeneratedValue
    @Column(unique = true)
    private Integer id;

    @OneToOne
    @JoinColumn(name="account_id")
    private Account account;

    @OneToMany( mappedBy = "shop")
    private Set<Product> products = new HashSet<>();

    @OneToMany(mappedBy = "shop")
    private Set<Supplier> suppliers = new HashSet<>();

    @Column(name = "shop_name", unique = true)
    private String shopName;

    @Column(name = "website_url")
    private String websiteUrl;

    @Column(name = "image_url")
    private String imageUrl;

    @Column(name = "province_id")
    private String provinceId;

    @Column(name = "district_id")
    private String districtId;

    @Column(name = "ward_id")
    private String wardId;

    @Column(name = "delete_at")
    private String deteleAt;

    @Column(name = "create_at")
    private String createAt;

}
