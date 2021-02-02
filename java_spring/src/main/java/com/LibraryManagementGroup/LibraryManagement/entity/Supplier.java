package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;
import org.springframework.context.annotation.Primary;

import javax.persistence.*;
import java.util.Date;
import java.util.List;
@Setter
@Getter
@Entity
@Table(name="supplier")
public class Supplier {
    @Id
    @GeneratedValue
    private int id;

    @OneToMany(mappedBy = "supplier", cascade = CascadeType.ALL)
    private List<Book> books;

    private String address;
    private String phone;
    private String email;
    private String contact_name;
    private String description;
    private String note;
    private Date deteled_at;
}
