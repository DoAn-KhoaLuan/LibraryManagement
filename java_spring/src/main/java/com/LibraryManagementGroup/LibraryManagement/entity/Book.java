package com.LibraryManagementGroup.LibraryManagement.entity;

import java.util.Date;
import java.util.List;
import java.util.Set;

import javax.persistence.*;

@Entity
@Table(name="book")
public class Book {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name="category_id")
    private Category category;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name="author_id")
    private Author author;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name="supplier_id")
    private Supplier supplier;

    @OneToMany(mappedBy = "book")
    private List<StocktakeTicketDetail> stocktake_tickets_details;

    @OneToMany(mappedBy = "book")
    private List<OrderDetail> order_details;

    @OneToMany(mappedBy = "book")
    private List<BorrowTicketDetail> borrow_ticket_detail;
    private String book_name;
    private int old_amount;
    private String image;
    private int page_number;
    private String description;
    private Date delete_at;
    private String note;


}
