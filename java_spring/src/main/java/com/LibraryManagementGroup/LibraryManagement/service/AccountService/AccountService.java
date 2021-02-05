package com.LibraryManagementGroup.LibraryManagement.service.AccountService;

import com.LibraryManagementGroup.LibraryManagement.common.response.accountresponses.RegisterAccountResponse;
import com.LibraryManagementGroup.LibraryManagement.entity.Account;
import com.LibraryManagementGroup.LibraryManagement.repository.AccountRepository;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AccountService implements IAccountService {
    @Autowired
    AccountRepository accountRepository;

    @Override
    public RegisterAccountResponse registerAccount(Account accountEntity) {
        ModelMapper modelMapper = new ModelMapper();
        Account resAcc = accountRepository.saveAndFlush(accountEntity);

        RegisterAccountResponse resDTO = modelMapper.map(resAcc, RegisterAccountResponse.class);
        return resDTO;
    }
}
