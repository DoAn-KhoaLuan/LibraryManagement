package com.LibraryManagementGroup.LibraryManagement.common.requests.accountrequests;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class LoginRequest {
    private String username;
    private String password;
}
