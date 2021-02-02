package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.Date;
@Setter
@Getter
@Entity
@Table(name="message")
public class Message {
    @Id
    @GeneratedValue
    private int id;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name="conversation_id")
    private Conversation conversation;

    private String content;

    private Date created_at;

    private Date updated_at;

    private Date deleted_at;


}