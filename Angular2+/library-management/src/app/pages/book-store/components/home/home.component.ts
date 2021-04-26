import { Component, OnInit } from '@angular/core';
import {BookQuery} from "../../../../states/book-store/book.query";
import {BookService} from "../../../../states/book-store/book.service";
import {BookStore} from "../../../../states/book-store/book.store";
import { StarRatingComponent } from 'ng-starrating';
import {ActivatedRoute, Router} from "@angular/router";
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  book_list_view$ = this.bookQuery.book_list_view$;
  categories$ = this.bookQuery.categories$;
  constructor(
    private bookQuery: BookQuery,
    private bookService: BookService,
    private bookStore: BookStore,
    private router: Router
  ) { }

  async ngOnInit() {
    await this.bookService.getBooks(this.bookQuery.getValue().filter_page);
  }

  async getMore() {
    this.bookService.setGetMoreFilter();
    await this.bookService.getMore().then(_ => {
      console.log(this.bookQuery.getValue().book_list_view)
    });
  }

  onRate($event:{oldValue:number, newValue:number, starRating:StarRatingComponent}) {
    alert(`Old Value:${$event.oldValue},
      New Value: ${$event.newValue},
      Checked Color: ${$event.starRating.checkedcolor},
      Unchecked Color: ${$event.starRating.uncheckedcolor}`);
  }
  onDetail(id) {
    this.router.navigateByUrl("/book-store/detail/" + id);
  }
}
