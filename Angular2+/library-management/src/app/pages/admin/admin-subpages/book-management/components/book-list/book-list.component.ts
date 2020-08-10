import { Router } from '@angular/router';
import { PaginationOpt, NavigationDirection } from './../../../../../../shared/page-pagination/page-pagination.component';
import { Subject } from 'rxjs';
import { ApiBookService } from './../../../../../../API/api-book.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-book-list',
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.scss']
})
export class BookListComponent implements OnInit {
  filter_page = {
    page: 1,
    per_page: 1,
  }

  currentPage = 1;
  book_list = [];
  paginationOpt = new Subject<PaginationOpt>();

  has_next: boolean;
  has_prev: boolean

  currentPaginationOpt = new PaginationOpt();


  constructor(private ApiBookService: ApiBookService, private router: Router) { }

  async ngOnInit() {
    let res = await this.ApiBookService.GetBooks(this.filter_page)
    this.book_list = res['self.items'];
    this.has_next = res['has_next']
    this.has_prev = res['has_prev']
    this.setupPagination()
  }

  async navigate(direction) {
    switch (direction) {
      case NavigationDirection.BACKWARD:
        this.currentPage--;
        break;
      case NavigationDirection.FORWARD:
        this.currentPage++;
        break;
    }
    this.currentPage = this.currentPage <= 0 ? 1 : this.currentPage;
    this.filter_page.page = this.currentPage;
    await this.onRequestNewPage().then(() => {
      this.currentPaginationOpt = {
        hidePerpage: true,
        nextDisabled:  !this.has_next,
        previousDisabled: !this.has_prev,
      };
      this.paginationOpt.next(this.currentPaginationOpt);
    });
  }
  async onRequestNewPage() {
    let res = await this.ApiBookService.GetBooks(this.filter_page)
    this.book_list = res['self.items'];
    this.has_next = res['has_next']
    this.has_prev = res['has_prev']
    this.setupPagination()
  }

  setupPagination() {
    this.currentPaginationOpt = {
      hidePerpage: true,
      nextDisabled:  !this.has_next,
      previousDisabled: !this.has_prev,
    };
    this.paginationOpt.next(this.currentPaginationOpt)
  }

  onViewBookDetail(book_id) {
    this.router.navigateByUrl(`/admin/book-management/book-detail/${book_id}`);
  }
}