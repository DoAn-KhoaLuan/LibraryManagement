package com.LibraryManagementGroup.LibraryManagement.controller;

import com.LibraryManagementGroup.LibraryManagement.JWTConfiguration.JwtUtil;
import com.LibraryManagementGroup.LibraryManagement.JWTConfiguration.MyUserDetailsService;
import com.LibraryManagementGroup.LibraryManagement.common.requests.accountrequests.LoginRequest;
import com.LibraryManagementGroup.LibraryManagement.common.response.accountresponses.LoginResponse;
import com.LibraryManagementGroup.LibraryManagement.common.response.accountresponses.RegisterAccountResponse;
import com.LibraryManagementGroup.LibraryManagement.entity.Account;
import com.LibraryManagementGroup.LibraryManagement.service.AccountService.AccountService;
import net.minidev.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/admin/account-management")
public class AccountController {
    @Autowired
    private AuthenticationManager authenticationManager;

    @Autowired
    AccountService accountService;

    @Autowired
    MyUserDetailsService myUserDetailsService;

    @Autowired
    private JwtUtil jwtTokenUtil;

    @PostMapping("/login")
    public ResponseEntity<?> loginAccount(@RequestBody LoginRequest loginReq) throws Exception {
        try {
            System.out.println("loginAccount");

            authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(loginReq.getUsername(), loginReq.getPassword()));
            RegisterAccountResponse account = accountService.getAccountByAccountName(loginReq.getUsername());
            UserDetails userDetails = myUserDetailsService.loadUserByUsername(loginReq.getUsername());
            String jwt = jwtTokenUtil.generateToken(userDetails);
            LoginResponse loginRes = new LoginResponse(jwt, account);
            JSONObject resObj = new JSONObject();

            resObj.put("accessToken", jwt);
            resObj.put("account", account);

            return ResponseEntity.ok(resObj);
        } catch (BadCredentialsException e) {
            throw new Exception("Incorrect username or password");
        }
    }

    @PostMapping("/register")
    public ResponseEntity<?> registerAccount(@RequestBody Account accountReq) {
        try {
            RegisterAccountResponse res = accountService.registerAccount(accountReq);
            return ResponseEntity.ok(res);
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.badRequest().body(e.getMessage());
        }

    }
}
