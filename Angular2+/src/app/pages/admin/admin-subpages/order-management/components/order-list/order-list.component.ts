import { Router } from '@angular/router';
import { PaginationOpt, NavigationDirection } from '../../../../../../shared/page-pagination/page-pagination.component';
import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { OrderService } from 'src/app/states/order-store/order.service';
import { OrderQuery } from 'src/app/states/order-store/order.query';
import { OrderStore } from 'src/app/states/order-store/order.store';
import {FormBuilder} from "@angular/forms";

@Component({
  selector: 'app-order-list',
  templateUrl: './order-list.component.html',
  styleUrls: ['./order-list.component.scss']
})
export class OrderListComponent implements OnInit {
  order_list$ = this.OrderQuery.order_list_view$;
  current_pagination_opt$ = this.OrderQuery.current_pagination_opt$;
  current_page$ = this.OrderQuery.current_page$;
  currentPaginationOpt = new PaginationOpt();
  orderTypes = [
    {
      display_name: "Tại chỗ",
      type_name: "offline"
    },
    {
      display_name: "Trực tuyến",
      type_name: "online"
    },
  ]

  searchForm = this.fb.group({
    order_id: '',
    customer_phone: '',
    type: '',
  });

  constructor(
    private fb: FormBuilder,
    private router: Router, private OrderService: OrderService, private OrderQuery: OrderQuery, private OrderStore: OrderStore, private ref: ChangeDetectorRef) { }

  async ngOnInit() {
    await this.onRequestNewPage();
  }

  async onRequestNewPage() {
    await this.OrderService.getOrders(this.OrderQuery.getValue().filter_page).then(() => {
      this.OrderService.setupPagination();
    })
  }

  async navigate(direction) {
    this.OrderService.navigate(direction);
    await this.onRequestNewPage()
  }

  onViewOrderDetail(order_id) {
    this.router.navigateByUrl(`/admin/order-management/order-detail/${order_id}`);
  }

  async search() {
    let {
      order_id,
      customer_phone,
      type
    } = this.searchForm.value;
    if (!order_id && !customer_phone && !type) {
      return await this.onRequestNewPage();
    }
    const req = {
      order_id: order_id || null,
      customer_phone: customer_phone || null,
      type: type || null
    };
    let orders = await this.OrderService.searchOrders(req);
    this.OrderStore.update({
      order_list_view: {
        items: orders,
        has_next: false,
        has_prev: false,
        current_page: 1
      }
    });
  }
}
