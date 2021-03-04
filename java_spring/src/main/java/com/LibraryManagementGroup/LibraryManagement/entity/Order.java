package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.Date;
import java.util.HashSet;
import java.util.Set;

@Setter
@Getter
@Entity
@Table(name = "shop_order")
public class Order {
    @Id
    @GeneratedValue
    @Column(unique = true)
    private Integer id;

    @ManyToOne
    @JoinColumn(name="customer_id", nullable = false)
    private Account customerAccount;

    @ManyToOne
    @JoinColumn(name="shop_id", nullable = false)
    private Account shopAccount;

    @OneToMany(mappedBy = "order")
    private Set<OrderDetail> orderDetails = new HashSet<>();

    @Column(name = "total")
    private Float total;

    @Column(name = "type")
    private OrderType type;

    @Column(name = "delete_at")
    private String deteleAt;

    @Column(name = "create_at")
    private String createAt;
}
