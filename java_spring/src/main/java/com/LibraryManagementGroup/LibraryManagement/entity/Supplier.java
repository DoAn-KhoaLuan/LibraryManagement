package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Setter
@Getter
@Entity
@Table(name = "supplier")
public class Supplier {
    @Id
    @GeneratedValue
    @Column(unique = true)
    private Integer id;

    @OneToMany( mappedBy = "supplier")
    private Set<Product> products= new HashSet<>();

    @Column(name = "delete_at")
    private String deteleAt;

    @Column(name = "create_at")
    private String createAt;

    @ManyToOne
    @JoinColumn(name = "shop_id")
    private Shop shop;
}
