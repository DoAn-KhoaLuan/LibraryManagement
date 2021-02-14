package com.LibraryManagementGroup.LibraryManagement.common.requests.accountrequests;

import com.LibraryManagementGroup.LibraryManagement.entity.Comment;
import com.LibraryManagementGroup.LibraryManagement.entity.Order;
import com.LibraryManagementGroup.LibraryManagement.entity.RoleName;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.Column;
import javax.persistence.OneToMany;
import java.util.Date;
import java.util.Set;

@Getter
@Setter
public class RegisterAccountRequest {
    private String provinceId;

    private String districtId;

    private String wardId;

    private String address;

    private RoleName roleName;

    private String accountName;

    private String accountPassword;

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
