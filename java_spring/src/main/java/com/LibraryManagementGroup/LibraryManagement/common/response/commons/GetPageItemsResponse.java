package com.LibraryManagementGroup.LibraryManagement.common.response.commons;

import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Setter
@Getter
public class GetPageItemsResponse {
    private Boolean has_next;
    private Boolean has_prev;
    private List[] items;
    private Integer current_page;
}
