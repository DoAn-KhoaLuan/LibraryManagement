import { Component, OnInit } from '@angular/core';
import { BookQuery } from '../../../../states/book-store/book.query';
import { Router } from '@angular/router';
import { BookService } from '../../../../states/book-store/book.service';
import { BookStore } from '../../../../states/book-store/book.store';
import { SupplierService } from '../../../../states/supplier-store/supplier.service';
import { SupplierQuery } from '../../../../states/supplier-store/supplier.query';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss'],
})
export class SearchComponent implements OnInit {
  book_id = '';
  searchKeyword = '';
  category_id = '';
  supplier_id = '';
  from_price = 0.0;
  to_price = 0.0;
  book_list_view$ = this.bookQuery.book_list_view$;
  suppliers$ = this.supplierQuery
    .select('supplier_list_view')
    .pipe(map((view) => view?.items));

  categories$ = this.bookQuery.categories$;
  constructor(
    private bookQuery: BookQuery,
    private router: Router,
    private bookService: BookService,
    private bookStore: BookStore,
    private supplierService: SupplierService,
    private supplierQuery: SupplierQuery
  ) {}

  async ngOnInit() {
    await this.bookService
      .getBooks({
        page: 1,
        per_page: 20,
      })
      .then(() => {});
    await this.supplierService
      .GetSuppliers(this.supplierQuery.getValue().filter_page)
      .then(() => {});
  }

  onDetail(id) {
    this.router.navigateByUrl('/book-store/detail/' + id);
  }

  async SearchBooks() {
    if (this.from_price > this.to_price) {
      return toastr.error('Khoảng giá tiền sản phẩm không hợp lệ');
    }
    const req = {
      book_id: this.book_id || null,
      book_name: this.searchKeyword || null,
      category_id: this.category_id || null,
      supplier_id: this.supplier_id || null,
      from_price: this.from_price || null,
      to_price: this.to_price || null,
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
  }
}
