package com.LibraryManagementGroup.LibraryManagement.dto.bookdto;

import com.LibraryManagementGroup.LibraryManagement.entity.Book;
import lombok.Getter;
import lombok.Setter;

import java.util.Date;
import java.util.List;
@Setter
@Getter
public class AuthorDto {
    private List<Book> books;

    private String author_name;

    private Date deleted_at;
}
