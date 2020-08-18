import { async } from '@angular/core/testing';
import { BookStore } from './../../../../../../states/book-store/book.store';
import { BookQuery } from './../../../../../../states/book-store/book.query';
import { BookService } from './../../../../../../states/book-store/book.service';
import { Router } from '@angular/router';
import { PaginationOpt, NavigationDirection } from './../../../../../../shared/page-pagination/page-pagination.component';
import { Subject } from 'rxjs';
import { ApiBookService } from './../../../../../../API/api-book.service';
import { Component, OnInit, ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-book-list',
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.scss']
})
export class BookListComponent implements OnInit {
  book_list$ = this.bookQuery.book_list_view$;
  current_pagination_opt$ = this.bookQuery.current_pagination_opt$;
  current_page$ = this.bookQuery.current_page$;
  currentPaginationOpt = new PaginationOpt();

  constructor(private router: Router, private bookService: BookService, private bookQuery: BookQuery, private bookStore: BookStore, private ref: ChangeDetectorRef) { }

  async ngOnInit() {
    await this.onRequestNewPage();
  }

  async onRequestNewPage() {
    await this.bookService.getBooks(this.bookQuery.getValue().filter_page).then(() => {
      this.bookService.setupPagination();
    })
  }

  async navigate(direction) {
    this.bookService.navigate(direction);
    await this.onRequestNewPage()
  }

  onViewBookDetail(book_id) {
    this.router.navigateByUrl(`/admin/book-management/book-detail/${book_id}`);
  }
}