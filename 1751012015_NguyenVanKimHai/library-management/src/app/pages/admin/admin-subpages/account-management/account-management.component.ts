import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-account-management',
  templateUrl: './account-management.component.html',
  styleUrls: ['./account-management.component.scss']
})
export class AccountManagementComponent implements OnInit {
  headerItems = [
    {
      itemName: "Danh sách tài khoản",
      url: "account-list"
    },
    {
      itemName: "Tạo mới thông tin tài khoản",
      url: "create-account"
    },
    {
      itemName: "Danh sách khách hàng",
      url: "customer-list"
    },
    {
      itemName: "Danh sách nhân viên",
      url: "employee-list"
    },
  ]
  constructor() { }

  ngOnInit() {
  }

}
