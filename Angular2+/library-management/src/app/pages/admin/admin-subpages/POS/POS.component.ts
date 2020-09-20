import { CustomerStore } from './../../../../states/customer-store/customer.store';
import { BookStore } from './../../../../states/book-store/book.store';
import { BookService } from './../../../../states/book-store/book.service';
import { Component, OnInit } from '@angular/core';
import { CustomerService } from 'src/app/states/customer-store/customer.service';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-POS',
  templateUrl: './POS.component.html',
  styleUrls: ['./POS.component.scss']
})
export class POSComponent implements OnInit {

  constructor(
    private bookService: BookService,
    private bookStore: BookStore,
    private customerService: CustomerService,
    private customerStore: CustomerStore,
    private fb: FormBuilder
  ) { }

  ngOnInit() {
  }

}
