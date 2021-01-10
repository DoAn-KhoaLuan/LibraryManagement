package com.LibraryManagementGroup.LibraryManagement.entity;

import java.util.Date;
import java.util.Set;

import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@Entity
@Table(name="book")
public class Book {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    private String book_name;
    private int old_amount;
    private String image;
    private int page_number;
    private String description;
    private Date delete_at;
    private String note;

    public Book() {

    }

    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getBook_name() {
        return book_name;
    }
    public void setBook_name(String book_name) {
        this.book_name = book_name;
    }
    public int getOld_amount() {
        return old_amount;
    }
    public void setOld_amount(int old_amount) {
        this.old_amount = old_amount;
    }

    public String getImage() {
        return image;
    }
    public void setImage(String image) {
        this.image = image;
    }
    public int getPage_number() {
        return page_number;
    }
    public void setPage_number(int page_number) {
        this.page_number = page_number;
    }
    public String getDescription() {
        return description;
    }
    public void setDescription(String description) {
        this.description = description;
    }

    public Date getDelete_at() {
        return delete_at;
    }
    public void setDelete_at(Date delete_at) {
        this.delete_at = delete_at;
    }
    public String getNote() {
        return note;
    }
    public void setNote(String note) {
        this.note = note;
    }



}
