import { Component, OnInit } from '@angular/core';
import {BookQuery} from "../../../../states/book-store/book.query";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  categories$ = this.bookQuery.categories$
  constructor(
    private bookQuery: BookQuery
  ) { }

  ngOnInit(): void {
  }

}
