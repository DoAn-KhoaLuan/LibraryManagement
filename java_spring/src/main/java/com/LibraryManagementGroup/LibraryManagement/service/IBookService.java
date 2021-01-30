package com.LibraryManagementGroup.LibraryManagement.service;

import com.LibraryManagementGroup.LibraryManagement.common.requests.commons.GetPageItemsRequest;
import com.LibraryManagementGroup.LibraryManagement.entity.Author;
import net.minidev.json.JSONObject;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;

@Component
public interface IBookService {
    public List<Author> getAuthors(GetPageItemsRequest req);
}
