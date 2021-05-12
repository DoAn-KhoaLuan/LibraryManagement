import { Component, OnInit } from '@angular/core';
import { BookQuery } from '../../../../states/book-store/book.query';
import { BookService } from '../../../../states/book-store/book.service';
import { Router } from '@angular/router';
import { BookStore } from '../../../../states/book-store/book.store';
import {AccountQuery} from "../../../../states/account-store/account.query";
import {AccountService} from "../../../../states/account-store/account.service";

@Component({
  selector: 'app-shop-header',
  templateUrl: './shop-header.component.html',
  styleUrls: ['./shop-header.component.scss'],
})
export class ShopHeaderComponent implements OnInit {
  categories$ = this.bookQuery.categories$;
  auth_info$ = this.auth.auth_info$
  book_name = '';
  constructor(
    private bookQuery: BookQuery,
    private bookService: BookService,
    private router: Router,
    private bookStore: BookStore,
    private auth: AccountQuery,
    private accountService: AccountService,
  ) {}

  ngOnInit(): void {
  }

  async searchBooksByCategoryID(category_id) {
    const req = {
      category_id : category_id || null,
    };
    let books = await this.bookService.searchBooks(req);
    let book_view = this.bookStore.getValue().book_list_view;
    this.bookStore.update({
      book_list_view: {
        ...book_view,
        items: books.books,
        has_next: false,
        has_prev: false,
        current_page: 1,
      },
    });
    this.router.navigateByUrl('/book-store/search');
  }

  goToCheckOut() {
    this.router.navigateByUrl('/book-store/checkout');
  }

  goToRegisterView() {
    this.router.navigateByUrl('/user/register');
  }

  goToLoginView() {
    this.router.navigateByUrl('/user/login');
  }
  logout() {
    this.accountService.Logout()
  }

  async SearchBooks() {
    if(!this.book_name ) {
      return
    }
    const req = {
      book_name: this.book_name || null,
    }
    let books = await this.bookService.searchBooks(req);
    let book_view = this.bookStore.getValue().book_list_view;
    if(books.books.length) {
      this.bookStore.update({
        book_list_view: {...book_view,
          items: books.books,
          has_next: false,
          has_prev: false,
          current_page: 1
        },
      })
    } else {
      this.bookStore.update({
        book_list_view: {...book_view,
          items: [],
          has_next: false,
          has_prev: false,
          current_page: 1
        },
      })
    }
    this.router.navigateByUrl('/book-store/search');
  }
}
