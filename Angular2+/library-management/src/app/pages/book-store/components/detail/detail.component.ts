import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Route} from "@angular/router";
import {BookService} from "../../../../states/book-store/book.service";
import {BookQuery} from "../../../../states/book-store/book.query";
import {ApiBookService} from "../../../../API/api-book.service";

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.scss'],
})
export class DetailComponent implements OnInit {
  stars: number[] = [1, 2, 3, 4, 5];

  book_id;
  detailBook$ = this.bookQuery.detail_book$
  quantity = 0;
  selectedStar: number;
  constructor(
    private route: ActivatedRoute,
    private bookService: BookService,
    private bookQuery: BookQuery,
    private apiBookService: ApiBookService
  ) {}

  async ngOnInit() {
    const req = {
      book_id: parseInt(this.route.snapshot.params['id'])
    }
    this.book_id = req.book_id;
    const res = await this.bookService.getBookByID(req);
    const detail_book = res;
    this.bookService.setDetailBook(detail_book);
  }

  IncreaseQuantity() {
    if (this.quantity >= this.bookQuery.getValue().detail_book.new_amount) {
      return toastr.error('Số lượng hàng tồn kho không đủ!');
    }
    this.quantity += 1;
  }

  DecreaseQuantity() {
    if (this.quantity == 0) {
      return;
    }
    this.quantity -= 1;
  }

  ChangeQuantity(order_line) {
    this.quantity = this.quantity < 0 ? Math.abs(this.quantity) : this.quantity;
  }

  addToChart() {
    if (this.quantity == 0) {
      toastr.error("Vui lòng chọn số lượng sản phẩm")
    }
    let order_details = [];
    order_details = JSON.parse(localStorage.getItem("order_details")) || []
    order_details.push({
      book: this.bookQuery.getValue().detail_book,
      quantity: this.quantity
    });
    localStorage.setItem("order_details", JSON.stringify(order_details))
  }

  countStar(star) {
    this.selectedStar = star;
    console.log('Value of star', star);
  }

  async rateStar() {
    if (!localStorage.getItem("auth_info")) {
      return toastr.error("Vui lòng đăng nhập để đánh giá sảm phẩm")
    }
    if (!this.selectedStar) {
      return toastr.error("Vui lòng chọn sao cho sản phẩm")
    }

    const req = {
      id: this.book_id,
      star: this.selectedStar
    }

    await this.apiBookService.rateStar(req).then(_ => {
      toastr.success("Đánh giá sản phẩm thành công")
      this.selectedStar = 0
    })
  }
}
