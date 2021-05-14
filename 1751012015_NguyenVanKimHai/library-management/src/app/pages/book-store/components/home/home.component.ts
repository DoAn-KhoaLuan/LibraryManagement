import { Component, OnInit } from '@angular/core';
import {BookQuery} from "../../../../states/book-store/book.query";
import {BookService} from "../../../../states/book-store/book.service";
import {BookStore} from "../../../../states/book-store/book.store";
import {ActivatedRoute, Router} from "@angular/router";
import {TelegramService} from '../../../../services/telegram.service';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  special_books = [
    {
      "image_1": "https://salt.tikicdn.com/cache/280x280/ts/product/dd/bd/d4/58b7fd001b10463802671c72792fbed2.png",
      "image_2": "https://salt.tikicdn.com/cache/280x280/ts/product/95/5b/74/b43e9b368d9a77d6d0a9cf72a9c7570d.jpg",
      "image_3": "https://salt.tikicdn.com/cache/280x280/ts/product/0e/ad/12/e7a0d987f0b9d4ee7005711c5ed552c9.png",
      "title": "Sách makeup",
      "amount": 139,
    },
    {
      "image_1": "https://salt.tikicdn.com/cache/280x280/ts/product/fc/fd/5c/b7ef930bface9d5e9674a0296ae78544.jpg",
      "image_2": "https://salt.tikicdn.com/cache/280x280/ts/product/0e/91/ae/4ab64ddcd9c9dc751f5d2e679e763ede.jpg",
      "image_3": "https://salt.tikicdn.com/cache/280x280/ts/product/09/56/38/60b0caeaa9987ad1c01f331094a27796.jpg",
      "title": "Đọc vị bất kỳ ai",
      "amount": 314,
    },
    {
      "image_1": "https://salt.tikicdn.com/cache/280x280/ts/product/9b/93/fa/b3cca812a20efd0ec37f1fd7e8595fd4.jpg",
      "image_2": "https://salt.tikicdn.com/cache/280x280/ts/product/15/11/f8/56b303e000cb42faada663569fc5d7c9.jpg",
      "image_3": "https://salt.tikicdn.com/cache/280x280/ts/product/1b/a1/1a/7b7944796ca2b3148055cc5d7e2b47d5.jpg",
      "title": "Biết chính mình",
      "amount": 105,
    },
  ]

  book_list_view$ = this.bookQuery.book_list_view$;
  categories$ = this.bookQuery.categories$;
  constructor(
    private bookQuery: BookQuery,
    private bookService: BookService,
    private bookStore: BookStore,
    private router: Router,
    private telegramService: TelegramService,
  ) { }

  async ngOnInit() {
    const  filter = {
      ...this.bookQuery.getValue().filter_page,
      page: 1,
      per_page: 12
    };
    this.bookStore.update({filter_page: filter});
    // await this.telegramService.testMessage();
    await this.bookService.getBooks(filter);
  }

  async getMore() {
    this.bookService.setGetMoreFilter();
    await this.bookService.getMore().then(_ => {
    });
  }

  onDetail(id) {
    this.router.navigateByUrl("/book-store/detail/" + id);
  }
}
