package com.LibraryManagementGroup.LibraryManagement.entity;

import org.springframework.context.annotation.Primary;

import javax.persistence.*;
import java.util.Date;

@Entity
@Table(name="borrow_ticket_detail")
public class BorrowTicketDetail {
    @Id
    @GeneratedValue
    private int id;


    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "borrow_ticket_id")
    private BorrowTicket borrow_ticket;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "book_id")
    private Book book;

    private Date deleted_at;
}
