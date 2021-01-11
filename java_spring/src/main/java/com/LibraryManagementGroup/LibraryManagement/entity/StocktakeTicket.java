package com.LibraryManagementGroup.LibraryManagement.entity;

import javax.persistence.*;
import java.util.Date;
import java.util.List;

@Entity
@Table(name="stocktake_ticket")
public class StocktakeTicket {

    @Id
    @GeneratedValue
    private int id;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "employee_id")
    private Employee employee;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "customer_id")
    private Customer customer;

    @OneToMany(mappedBy = "stocktake_ticket")
    private List<StocktakeTicketDetail> stocktake_ticket_details;

    private String stock_take_type;

    private String book_type;

    private Date date;

    private float disparity_price;

    private Date deteled_at;

}
