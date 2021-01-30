package com.LibraryManagementGroup.LibraryManagement.repository;


import com.LibraryManagementGroup.LibraryManagement.entity.Author;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.Date;
import java.util.List;

public interface AuthorRepository extends JpaRepository<Author, Integer> {
    @Query("select a from Author a")
    List<Author> getAllByDelete_atIs(Date date);
}
