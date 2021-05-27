import { CustomerService } from '../../../../../../states/customer-store/customer.service';
import { CustomerStore } from '../../../../../../states/customer-store/customer.store';
import { CustomerQuery } from '../../../../../../states/customer-store/customer.query';
import { Router } from '@angular/router';
import { PaginationOpt } from '../../../../../../shared/page-pagination/page-pagination.component';
import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import {FormBuilder} from "@angular/forms";

@Component({
  selector: 'app-customer-list',
  templateUrl: './customer-list.component.html',
  styleUrls: ['./customer-list.component.scss']
})
export class CustomerListComponent implements OnInit {
  customer_list$ = this.customerQuery.customer_list_view$;
  current_pagination_opt$ = this.customerQuery.current_pagination_opt$;
  current_page$ = this.customerQuery.current_page$;
  currentPaginationOpt = new PaginationOpt();
  searchForm = this.fb.group({
    customer_id: '',
    phone: '',
  });
  constructor(
    private fb: FormBuilder,
    private router: Router,
    private ref: ChangeDetectorRef,
    private customerQuery: CustomerQuery,
    private customerStore: CustomerStore,
    private customerService: CustomerService) { }

  async ngOnInit() {
    await this.onRequestNewPage();
  }

  async onRequestNewPage() {
    await this.customerService.GetCustomers(this.customerQuery.getValue().filter_page).then(() => {
      this.customerService.setupPagination();
    })
  }

  async navigate(direction) {
    this.customerService.navigate(direction);
    await this.onRequestNewPage()
  }

  onViewCustomerDetail(customer_id) {
    this.router.navigateByUrl(`/admin/account-management/customer-detail/${customer_id}`);
  }
  async search() {
    let {
      customer_id,
      phone,
    } = this.searchForm.value;
    if (!customer_id && !phone) {
      return await this.onRequestNewPage();
    }
    const req = {
      customer_id: customer_id || null,
      phone: phone || null,
    };
    let customers = await this.customerService.SearchCustomers(req);
    this.customerStore.update({
      customer_list_view: {
        items: customers,
        has_next: false,
        has_prev: false,
        current_page: 1
      }
    });
  }
}
