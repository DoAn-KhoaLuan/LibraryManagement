package com.LibraryManagementGroup.LibraryManagement.service.AccountService;

import com.LibraryManagementGroup.LibraryManagement.common.response.accountresponses.RegisterAccountResponse;
import com.LibraryManagementGroup.LibraryManagement.entity.Account;
import com.LibraryManagementGroup.LibraryManagement.repository.AccountRepository;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.Optional;

@Service
public class AccountService implements IAccountService {
    @Autowired
    AccountRepository accountRepository;

    @Override
    public RegisterAccountResponse registerAccount(Account accountEntity) {
        ModelMapper modelMapper = new ModelMapper();

//        accountEntity.encodePassword();
        accountEntity.setCreateAt(new Date().toString());
        Account resAcc = accountRepository.saveAndFlush(accountEntity);
        RegisterAccountResponse resDTO = modelMapper.map(resAcc, RegisterAccountResponse.class);
        return resDTO;
    }

    public Account getAccountById(Integer accountId) {
        return accountRepository.getAccountById(accountId);
    }
    public RegisterAccountResponse getAccountByAccountName(String accountName) {
        ModelMapper modelMapper = new ModelMapper();
        Account resAcc = accountRepository.getAccountByAccountName(accountName);
        RegisterAccountResponse resDTO = modelMapper.map(resAcc, RegisterAccountResponse.class);
        return resDTO;
    }
}
