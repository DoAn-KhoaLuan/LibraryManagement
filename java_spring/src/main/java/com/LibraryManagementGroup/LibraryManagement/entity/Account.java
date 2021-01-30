package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;
import net.minidev.json.JSONObject;

import javax.persistence.*;
import java.util.Date;
import java.util.Map;

@Setter
@Getter
@Entity
@Table(name="account")
public class Account {
    @Id
    @GeneratedValue
    private int id;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name="role_id")
    private Role role;

    @OneToOne(cascade = CascadeType.ALL)
    @PrimaryKeyJoinColumn
    private Conversation conversation;

    private String account_name;

    private String account_password;

    private String note;

    private Date deleted_at;

}
