package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.Date;
import java.util.List;
@Setter
@Getter
@Entity
@Table(name="borrow_ticket")
public class BorrowTicket {
    @Id
    @GeneratedValue
    private int id;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "employee_id")
    private Employee employee;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "customer_id")
    private Customer customer;

    @OneToMany(mappedBy = "borrow_ticket")
    private List<BorrowTicketDetail> borrow_ticket_details;

    private int quantity;

    private Date borrow_date;

    private Date appointment_date;

    private Date return_date;

    private String note;

    private Date dateled_at;

}
