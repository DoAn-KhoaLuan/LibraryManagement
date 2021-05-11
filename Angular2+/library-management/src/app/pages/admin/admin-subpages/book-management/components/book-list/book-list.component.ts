import { BookStore } from './../../../../../../states/book-store/book.store';
import { BookQuery } from './../../../../../../states/book-store/book.query';
import { BookService } from './../../../../../../states/book-store/book.service';
import { Router } from '@angular/router';
import { PaginationOpt, NavigationDirection } from './../../../../../../shared/page-pagination/page-pagination.component';
import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import {ApiSupplierService} from "../../../../../../API/api-supplier.service";
import {SupplierQuery} from "../../../../../../states/supplier-store/supplier.query";
import {SupplierService} from "../../../../../../states/supplier-store/supplier.service";
import {map} from "rxjs/operators";

@Component({
  selector: 'app-book-list',
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.scss']
})
export class BookListComponent implements OnInit {
  book_list$ = this.bookQuery.book_list_view$;
  current_pagination_opt$ = this.bookQuery.current_pagination_opt$;
  categories$ = this.bookQuery.categories$;
  current_page$ = this.bookQuery.current_page$;
  suppliers$ = this.supplierQuery.select("supplier_list_view").pipe(map(view => view?.items));
  book_id = "";
  searchKeyword = '';
  category_id = "";
  supplier_id = "";
  constructor(private router: Router, private bookService: BookService, private bookQuery: BookQuery, private bookStore: BookStore, private ref: ChangeDetectorRef,
              private supplierService: SupplierService, private supplierQuery: SupplierQuery) { }

  async ngOnInit() {
    await this.onRequestNewPage();
  }

  async onRequestNewPage() {
    await this.bookService.getBooks(this.bookQuery.getValue().filter_page).then(() => {
      this.bookService.setupPagination();
    })
    await this.supplierService.GetSuppliers(this.supplierQuery.getValue().filter_page).then(() => {
    })
  }

  async SearchBooks() {
    if(!this.searchKeyword && !this.book_id && !this.category_id && !this.supplier_id) {
      return await this.onRequestNewPage();
    }
    const req = {
      book_id: this.book_id,
      book_name: this.searchKeyword,
      category_id: this.category_id,
      supplier_id: this.supplier_id
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

  }

  async navigate(direction) {
    this.bookService.navigate(direction);
    await this.onRequestNewPage()
  }

  onViewBookDetail(book_id) {
    this.router.navigateByUrl(`/admin/book-management/book-detail/${book_id}`);
  }
}
