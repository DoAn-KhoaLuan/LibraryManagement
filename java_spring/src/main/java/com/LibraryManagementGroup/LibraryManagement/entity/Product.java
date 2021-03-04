package com.LibraryManagementGroup.LibraryManagement.entity;
import java.util.*;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

@Setter
@Getter
@Entity
@Table(name = "product")
public class Product {
    @Id
    @GeneratedValue
    @Column(unique = true)
    private Integer id;

    @OneToMany(mappedBy = "product")
    private Set<Comment> comments = new HashSet<>();

    @OneToMany(mappedBy = "product")
    private Set<OrderDetail> orderDetails = new HashSet<>();

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "category_id")
    private Category category;

    @ManyToOne
    @JoinColumn(name = "shop_id")
    private Shop shop;

    @ManyToOne
    @JoinColumn(name = "supplier_id")
    private Supplier supplier;

    @ManyToMany(cascade = {
            CascadeType.PERSIST,
            CascadeType.MERGE
    })
    @JoinTable(name = "product_tag",
            joinColumns = @JoinColumn(name = "product_id"),
            inverseJoinColumns = @JoinColumn(name = "tag_id")
    )
    private List<Tag> tags = new ArrayList<>();

    @Column(name = "product_name")
    private String productName;

    @Column(name = "amount")
    private Integer amount;

    @Column(name = "image_url")
    private String imageUrl;

    @Column(name = "description")
    private String description;

    @Column(name = "cost_price")
    private Float costPrice;

    @Column(name = "retail_price")
    private Float retailPrice;

    @Column(name = "discount")
    private Float discount;

    @Column(name = "rate_star")
    private Float rateStart;

    @Column(name = "rate_count")
    private Integer rateCount;

    @Column(name = "note")
    private String note;

    @Column(name = "brand_name")
    private String brandName;

    @Column(name = "material")
    private String material;

    @Column(name = "size")
    private String size;

    @Column(name = "feature")
    private String feature;

    @Column(name = "origin")
    private String origin;

    @Column(name = "delete_at")
    private String deteleAt;

    @Column(name = "create_at")
    private String createAt;
}
