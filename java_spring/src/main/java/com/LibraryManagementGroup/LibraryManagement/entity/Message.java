package com.LibraryManagementGroup.LibraryManagement.entity;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.List;

@Setter
@Getter
@Entity
@Table(name = "message")
public class Message {
    @Id
    @GeneratedValue
    @Column(unique = true)
    private Integer id;

    @Column(name = "content", length = 1000)
    private String content;

    @Column(name = "delete_at")
    private String deteleAt;

    @Column(name = "create_at")
    private String createAt;
}
