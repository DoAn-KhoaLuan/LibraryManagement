package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.Date;
@Setter
@Getter
@Entity
@Table(name="stocktake_ticket_detail")
public class StocktakeTicketDetail {
    @Id
    @GeneratedValue
    private int id;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "stocktake_ticket_detail")
    private StocktakeTicket stocktake_ticket;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "book_id")
    private Book book;
    private int in_quantity;
    private int out_quantity;
    private int new_quantity;
    private int old_quantity;
    private Date deleted_at;
    private String note;

}
