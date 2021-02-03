package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

@Setter
@Getter
@Entity
@Table(name = "order_detail")
public class OrderDetail {
    @Id
    @GeneratedValue
    @Column(unique = true)
    private Integer id;

    @ManyToOne
    @JoinColumn(name = "order_id", nullable = false)
    private Order order;

    @ManyToOne
    @JoinColumn(name = "product_id", nullable = false)
    private Product product;

    @Column(name = "retail_price")
    private Float retailPrice;

    @Column(name = "quantity")
    private Integer quantity;

    @Column(name = "discount")
    private Float discount;

    @Column(name = "total")
    private Float total;

    @Column(name = "note", length = 1000)
    private String note;

    @Column(name = "create_at")
    private String createAt;
}
