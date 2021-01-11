package com.LibraryManagementGroup.LibraryManagement.entity;

import javax.persistence.*;
import java.util.Date;
import java.util.List;

@Entity
@Table(name = "conversation")
public class Conversation {
    @Id
    @GeneratedValue
    private int id;

    @OneToOne(mappedBy="conversation", cascade=CascadeType.ALL)
    private Account account;

    @OneToMany(mappedBy = "conversation")
    private List<Message> messages;

    private Date created_at;

    private Date updated_at;

    private String last_message;

    private boolean is_read;
}
