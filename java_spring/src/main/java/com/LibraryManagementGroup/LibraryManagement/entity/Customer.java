package com.LibraryManagementGroup.LibraryManagement.entity;

import javax.persistence.*;
import java.util.Date;
import java.util.List;

@Entity
@Table(name="customer")
public class Customer {
    @Id
    @GeneratedValue
    private int id;

    @OneToMany(mappedBy = "customer")
    private List<Schedule> schedules;

    @OneToMany(mappedBy = "customer")
    private List<StocktakeTicket> stocktake_tickets;

    @OneToMany(mappedBy = "customer")
    private List<Order> orders;

    @OneToMany(mappedBy = "customer")
    private List<BorrowTicket> borrow_tickets;

    @Column(nullable = false)
    private String identity_id;

    private String last_name;

    private String first_name;

    private String email;

    private String phone;

    private Date birth_date;

    private String address;

    private boolean gender;

    private String note;

    private Date deleted_at;
}
