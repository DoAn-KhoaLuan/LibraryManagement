package com.LibraryManagementGroup.LibraryManagement.entity;

import lombok.Getter;
import lombok.Setter;
import net.minidev.json.JSONObject;

import javax.persistence.*;
import java.util.Date;
import java.util.List;
import java.util.Map;
import java.util.Set;
@Setter
@Getter
@Entity
@Table(name="author")
public class Author {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @OneToMany(mappedBy = "author", cascade = CascadeType.ALL)
    private List<Book> books;

    private String author_name;

    private Date deleted_at;

    public JSONObject toObject() {
        JSONObject obj = new JSONObject();
        obj.put("id", id);
        obj.put("books", books);
        obj.put("authorName", author_name);
        obj.put("deletedAt", deleted_at);
        return obj;
    };

}
