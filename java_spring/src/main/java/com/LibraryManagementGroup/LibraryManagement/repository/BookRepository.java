package com.LibraryManagementGroup.LibraryManagement.repository;
import com.LibraryManagementGroup.LibraryManagement.entity.Author;
import com.LibraryManagementGroup.LibraryManagement.entity.Book;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public interface BookRepository extends JpaRepository<Book, Integer> {
}
