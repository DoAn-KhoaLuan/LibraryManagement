package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
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
    @JoinColumn(name="account_id", nullable = false)
    private Account account;

    @OneToMany(mappedBy = "shop")
    private Set<Product> productList;

    @OneToMany(mappedBy = "shop")
    private Set<ShopAddress> shopAddress;

    @Column(name = "shop_name")
    private String shopName;

    @Column(name = "website_url")
    private String websiteUrl;

    @Column(name = "image_url")
    private String imageUrl;

    @Column(name = "delete_at")
    private String deteleAt;

    @Column(name = "create_at")
    private String createAt;

}
