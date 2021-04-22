import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-customer-management',
  templateUrl: './customer-management.component.html',
  styleUrls: ['./customer-management.component.scss']
})
export class CustomerManagementComponent implements OnInit {
  headerItems = [
    {
      itemName: "Danh sản phẩm",
      url: "customer-list"
    },
  ]
  constructor() { }

  ngOnInit() {
  }

}
