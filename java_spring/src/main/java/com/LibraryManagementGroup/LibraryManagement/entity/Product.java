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

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "supplier_id")
    private Supplier supplier;

    @OneToMany(fetch = FetchType.LAZY ,mappedBy = "product")
    private Set<Comment> comments = new HashSet<>();

    @OneToMany(mappedBy = "product")
    private Set<OrderDetail> orderDetails = new HashSet<>();

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "category_id")
    private Category category;

    @ManyToOne
    @JoinColumn(name = "shop_id")
    private Shop shop;



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

    @Override
    public String toString() {
        return "Product{" +
                "id=" + id +
                ", comments=" + comments +
                ", orderDetails=" + orderDetails +
                ", category=" + category +
                ", shop=" + shop +
                ", supplier=" + supplier +
                ", tags=" + tags +
                ", productName='" + productName + '\'' +
                ", amount=" + amount +
                ", imageUrl='" + imageUrl + '\'' +
                ", description='" + description + '\'' +
                ", costPrice=" + costPrice +
                ", retailPrice=" + retailPrice +
                ", discount=" + discount +
                ", rateStart=" + rateStart +
                ", rateCount=" + rateCount +
                ", note='" + note + '\'' +
                ", brandName='" + brandName + '\'' +
                ", material='" + material + '\'' +
                ", size='" + size + '\'' +
                ", feature='" + feature + '\'' +
                ", origin='" + origin + '\'' +
                ", deteleAt='" + deteleAt + '\'' +
                ", createAt='" + createAt + '\'' +
                '}';
    }
}
