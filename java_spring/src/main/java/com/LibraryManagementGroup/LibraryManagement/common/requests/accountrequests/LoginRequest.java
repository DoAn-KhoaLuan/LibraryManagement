package com.LibraryManagementGroup.LibraryManagement.common.requests.accountrequests;

import lombok.Getter;
import lombok.Setter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

@Getter
@Setter
public class LoginRequest {
    private String username;
    private String password;

    public void encodePassword() {
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder(16);
        String encodedPassword = passwordEncoder.encode(this.getPassword());
        this.setPassword(encodedPassword);
    }
}
