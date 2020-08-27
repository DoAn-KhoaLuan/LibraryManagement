import { AccountService } from './../../../states/account-store/account.service';
import { Component, OnInit, Pipe } from '@angular/core';
import { Router } from '@angular/router';

@Pipe({
  name: 'wrapBold'
})
class WrapBold {
  transform(content) {
    return `<b>${content}</b>`;
  }
}

@Component({
  selector: 'app-sidebar-menu',
  templateUrl: './sidebar-menu.component.html',
  styleUrls: ['./sidebar-menu.component.scss']
})
export class SidebarMenuComponent implements OnInit {
  menuItems = [
    {
      iconHtml:`<i class="fa fa-2x fa-book" aria-hidden="true"></i>`,
      itemTitle: "Quản lý sách",
      routerLink: "book-management"
    },
    {
      iconHtml:`<i class="fa fa-2x fa-bookmark" aria-hidden="true"></i>`,
      itemTitle: "Quản lý khách hàng",
      routerLink: "customer-management"

    },
    {
      iconHtml:`<i class="fa fa-2x fa-ticket" aria-hidden="true"></i>`,
      itemTitle: "Quản lý mượn trả",
      routerLink: "service-management"

    },
    {
      iconHtml:`<i class="fa fa-2x fa-address-card" aria-hidden="true"></i>`,
      itemTitle: "Quản lý độc giả",
      routerLink: "employee-management"

    },
    {
      iconHtml:`<i class="fa fa-2x fa-truck" aria-hidden="true"></i>`,
      itemTitle: "Quản lý nhà cung cấp",
      routerLink: "supplier-management"

    },
    {
      iconHtml:`<i class="fa fa-2x fa-user" aria-hidden="true"></i>`,
      itemTitle: "Quản lý nhân viên",
      routerLink: "staff-management"

    },
    {
      iconHtml:`<i class="fa fa-2x fa-user-circle" aria-hidden="true"></i>`,
      itemTitle: "Quản lý tài khoản",
      routerLink: "account-management"

    },
    {
      iconHtml:`<i class="fa fa-2x fa-chart-line" aria-hidden="true"></i>`,
      itemTitle: "Thống kê",
      routerLink: "book-management"

    },
    
  ]
  constructor(
    private router: Router,
    private accountService: AccountService) { }

  ngOnInit() {
  }

  onRedirect(routerLink: string) {
    this.router.navigateByUrl('/admin/' + routerLink);
  }

  onLogout() {
   this.accountService.Logout();
  }
}
