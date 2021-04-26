import { Component, OnInit } from '@angular/core';
import {BookQuery} from "../../../../states/book-store/book.query";

@Component({
  selector: 'app-shop-header',
  templateUrl: './shop-header.component.html',
  styleUrls: ['./shop-header.component.scss']
})
export class ShopHeaderComponent implements OnInit {
  categories$ = this.bookQuery.categories$;
  constructor(
    private bookQuery: BookQuery
  ) { }

  ngOnInit(): void {
  }

}
