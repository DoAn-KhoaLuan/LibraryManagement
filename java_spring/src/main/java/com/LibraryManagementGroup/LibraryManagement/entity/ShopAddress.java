package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

@Setter
@Getter
@Entity
@Table(name = "shop_address")
public class ShopAddress {
    @Id
    @GeneratedValue
    @Column(unique = true)
    private Integer id;

    @ManyToOne
    @JoinColumn(name = "shop_id", nullable = false)
    private Shop shop;

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
