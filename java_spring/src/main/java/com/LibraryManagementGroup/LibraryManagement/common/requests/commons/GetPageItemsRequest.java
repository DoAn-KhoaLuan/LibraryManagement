package com.LibraryManagementGroup.LibraryManagement.common.requests.commons;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class GetPageItemsRequest {
    private int page;
    private int perPage;
}
