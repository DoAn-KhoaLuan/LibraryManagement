package com.LibraryManagementGroup.LibraryManagement.entity;

import javax.persistence.*;
import java.util.Date;

@Entity
@Table(name="schedule")
public class Schedule {
    @Id
    @GeneratedValue
    private int id;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "employee_id")
    private Employee employee;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "customer_id")
    private Customer customer;

    private Date date;
    private Date time_from;
    private Date time_to;
    private float actual_hour;
    private float expected_hour;
    private float salary;
    private Date deteled_at;
    private String note;
}
