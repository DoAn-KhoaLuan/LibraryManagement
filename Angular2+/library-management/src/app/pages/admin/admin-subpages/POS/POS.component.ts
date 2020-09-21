import { CustomerStore } from './../../../../states/customer-store/customer.store';
import { BookStore } from './../../../../states/book-store/book.store';
import { BookService } from './../../../../states/book-store/book.service';
import { Component, OnInit } from '@angular/core';
import { CustomerService } from 'src/app/states/customer-store/customer.service';
import {FormBuilder, FormControl} from '@angular/forms';
import {Observable} from "rxjs";
import {map, startWith, tap} from "rxjs/operators";
import {CustomerQuery} from "../../../../states/customer-store/customer.query";

@Component({
  selector: 'app-POS',
  templateUrl: './POS.component.html',
  styleUrls: ['./POS.component.scss']
})
export class POSComponent implements OnInit {
  all_customers = [];
  customer_control = new FormControl();
  customer_options: any[] = [];
  customer_filtered_options: Observable<string[]>;
  customer_item: any;


  filter = {
    page : 1,
    per_page: 1000
  }

  constructor(
    private bookService: BookService,
    private bookStore: BookStore,
    private customerService: CustomerService,
    private customerQuery: CustomerQuery,
    private fb: FormBuilder
  ) { }

  async ngOnInit() {
    await this.customerService.GetCustomers(this.filter);
    this.all_customers = this.customerQuery.getValue().customer_list_view.items;
    this.all_customers.forEach(customer => {
      let customer_option = {
        customer_id: customer.customer_id,
        last_name: customer.last_name,
        first_name: customer.first_name,
      }
      console.log(customer_option)
      this.customer_options.push(customer_option);
    })
    this.customer_filtered_options = this.customer_control.valueChanges.pipe(
      startWith(''),
      map(value => this._customerFilter(value)),
      tap(() => {
        if(this.customer_control.value){
          this.customer_item = this.all_customers.find(customer => customer.customer_id == parseInt(this.customer_control.value))
        }
      })
    );
  }

  private _customerFilter(value: string): string[] {
    return this.customer_options.filter(customer =>  customer.first_name.toString().toLowerCase().includes(value)  || customer.last_name.toString().includes(value) || customer.customer_id.toString().toLowerCase().includes(value));
  }

}
