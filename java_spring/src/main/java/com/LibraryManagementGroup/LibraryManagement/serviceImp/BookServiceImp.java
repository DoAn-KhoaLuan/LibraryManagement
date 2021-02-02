package com.LibraryManagementGroup.LibraryManagement.serviceImp;

import com.LibraryManagementGroup.LibraryManagement.common.requests.commons.GetPageItemsRequest;
import com.LibraryManagementGroup.LibraryManagement.entity.Author;
import com.LibraryManagementGroup.LibraryManagement.repository.AuthorRepository;
import com.LibraryManagementGroup.LibraryManagement.repository.BookRepository;
import com.LibraryManagementGroup.LibraryManagement.service.IBookService;
import net.minidev.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class BookServiceImp implements IBookService {
    @Autowired BookRepository bookRepository;
    @Autowired
    AuthorRepository authorRepository;

    @Override
    public List<Author> getAuthors(GetPageItemsRequest req) {
        List<Author> authorArr = authorRepository.getAllByDelete_atIs(null);
        return authorArr;
    }
}
