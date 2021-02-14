package com.LibraryManagementGroup.LibraryManagement.service.AccountService;

import com.LibraryManagementGroup.LibraryManagement.common.requests.accountrequests.RegisterAccountRequest;
import com.LibraryManagementGroup.LibraryManagement.common.response.accountresponses.RegisterAccountResponse;
import com.LibraryManagementGroup.LibraryManagement.entity.Account;
import org.springframework.stereotype.Component;

@Component
public interface IAccountService {
    public RegisterAccountResponse registerAccount(Account account);
}
