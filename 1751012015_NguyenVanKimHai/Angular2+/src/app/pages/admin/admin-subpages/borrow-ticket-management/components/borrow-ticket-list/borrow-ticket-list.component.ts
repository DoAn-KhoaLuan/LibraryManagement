import { async } from '@angular/core/testing';
import { BorrowTicketStore } from '../../../../../../states/borrow-ticket-store/borrow-ticket.store';
import { BorrowTicketQuery } from '../../../../../../states/borrow-ticket-store/borrow-ticket.query';
import { BorrowTicketService } from '../../../../../../states/borrow-ticket-store/borrow-ticket.service';
import { Router } from '@angular/router';
import { PaginationOpt, NavigationDirection } from '../../../../../../shared/page-pagination/page-pagination.component';
import { Subject } from 'rxjs';
import { ApiBorrowTicketService } from '../../../../../../API/api-borrow-ticket.service';
import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-borrow-ticket-list',
  templateUrl: './borrow-ticket-list.component.html',
  styleUrls: ['./borrow-ticket-list.component.scss']
})
export class BorrowTicketListComponent implements OnInit {
  borrow_ticket_list$ = this.borrowTicketQuery.borrow_ticket_list_view$;
  current_pagination_opt$ = this.borrowTicketQuery.current_pagination_opt$;
  current_page$ = this.borrowTicketQuery.current_page$;
  currentPaginationOpt = new PaginationOpt();

  searchForm = this.fb.group({
    customer_name: '',
    customer_phone: '',
    borrow_ticket_status: '',
  });

  ticketStatuses = [
    {
      display_name: "Đang mượn",
      borrow_ticket_status: "B"
    },
    {
      display_name: "Hoàn thành",
      borrow_ticket_status: "F"
    },
    {
      display_name: "Đang trễ",
      borrow_ticket_status: "L"
    },
    {
      display_name: "Trả trễ",
      borrow_ticket_status: "LF"
    },
  ]

  constructor(private router: Router, private borrowTicketService: BorrowTicketService, private borrowTicketQuery: BorrowTicketQuery, private borrowTicketStore: BorrowTicketStore, private ref: ChangeDetectorRef, private fb: FormBuilder) { }

  async ngOnInit() {
    await this.onRequestNewPage();
  }

  async onRequestNewPage() {
    await this.borrowTicketService.getBorrowTickets(this.borrowTicketQuery.getValue().filter_page).then(() => {
      this.borrowTicketService.setupPagination();
    })
  }

  async navigate(direction) {
    this.borrowTicketService.navigate(direction);
    await this.onRequestNewPage()
  }

  onViewBorrowTicketDetail(borrow_ticket_id) {
    this.router.navigateByUrl(`/admin/borrow-ticket-management/borrow-ticket-detail/${borrow_ticket_id}`);
  }

  async search() {
    let {
      customer_name,
      borrow_ticket_status,
      customer_phone
    } = this.searchForm.value;
    if (!customer_name && !borrow_ticket_status && !customer_phone) {
      return await this.onRequestNewPage();
    }
    const req = {
      customer_name: customer_name || null,
      borrow_ticket_status: borrow_ticket_status || null,
      customer_phone: customer_phone || null,
    };
    let tickets = await this.borrowTicketService.searchBorrowTickets(req);
    this.borrowTicketStore.update({
      borrow_ticket_list_view: {
        items: tickets.borrow_tickets,
        has_next: false,
        has_prev: false,
        current_page: 1
      }
    });
  }
}