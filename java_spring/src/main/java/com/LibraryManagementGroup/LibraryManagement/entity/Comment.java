package com.LibraryManagementGroup.LibraryManagement.entity;

import javax.persistence.*;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.List;
@Setter
@Getter
@Entity
@Table(name = "comment")
public class Comment {
    @Id
    @GeneratedValue
    @Column(unique = true)
    private Integer id;

    @ManyToOne
    @JoinColumn(name="product_id", nullable = false)
    private Product product;

    @ManyToOne
    @JoinColumn(name="customer_id", nullable = false)
    private Account account;

    @Column(name = "comment_title")
    private String commentTitle;

    @Column(name = "comment_content")
    private String commentContent;

    @Column(name = "delete_at")
    private String deteleAt;

    @Column(name = "create_at")
    private String createAt;
}
