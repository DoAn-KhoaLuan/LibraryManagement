import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  headerItems = [
    {
      itemName: "Thư quán",
      url: "sell-dashboard"
    },
    {
      itemName: "Thư viện",
      url: "management-dashboard"
    },
  ]
  constructor() { }

  ngOnInit() {
  }

}
