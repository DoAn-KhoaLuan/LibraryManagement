package com.LibraryManagementGroup.LibraryManagement.repository;

import com.LibraryManagementGroup.LibraryManagement.entity.Account;

import com.LibraryManagementGroup.LibraryManagement.entity.Author;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.Date;
import java.util.List;

@Repository
public interface AccountRepository extends JpaRepository<Account, Integer> {
    @Query("select a from Account a where id=?1")
    Account getAccountById(Integer id);

    @Query("select a from Account a where accountName=?1")
    Account getAccountByAccountName(String accountName);
}
