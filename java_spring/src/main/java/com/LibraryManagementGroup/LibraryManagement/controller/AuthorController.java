package com.LibraryManagementGroup.LibraryManagement.controller;

import com.LibraryManagementGroup.LibraryManagement.common.requests.commons.GetPageItemsRequest;
import com.LibraryManagementGroup.LibraryManagement.common.response.commons.GetPageItemsResponse;
import com.LibraryManagementGroup.LibraryManagement.entity.Author;
import com.LibraryManagementGroup.LibraryManagement.service.IBookService;
import net.minidev.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/admin/author-management")
public class AuthorController {
    @Autowired IBookService bookService;

    @PostMapping("/get-authors")
    public Object[] getAuthors(@RequestBody GetPageItemsRequest req) {
        List<Author> entityAuthorArr = bookService.getAuthors(req);
        JSONObject jsonObject = new JSONObject();
        GetPageItemsResponse res = new GetPageItemsResponse();
        return entityAuthorArr.toArray();
    }
}
