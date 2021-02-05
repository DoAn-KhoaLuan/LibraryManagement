package com.LibraryManagementGroup.LibraryManagement.common.response.accountresponses;

import com.LibraryManagementGroup.LibraryManagement.entity.RoleName;
import lombok.Getter;
import lombok.Setter;

import java.util.Date;

@Getter
@Setter
public class RegisterAccountResponse {
    private String provinceId;

    private String districtId;

    private String wardId;

    private String address;

    private RoleName roleName;

    private String accountName;

    private String lastName;

    private String firstName;

    private String phone;

    private String email;

    private Date birthDate;

    private String imageUrl;

    private String note;

    private String deteleAt;

    private String createAt;
}
