import { AccountService } from './states/account-store/account.service';
import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {BookService} from "./states/book-store/book.service";
import {ApiAccountService} from "./API/api-account.service";
import {LocationService} from './states/location-store';
import {SupplierService} from "./states/supplier-store/supplier.service";
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{

  constructor(private accountService: AccountService,
              private bookService: BookService,
              private apiAccountService: ApiAccountService,
              private locationService: LocationService,
              private supplierService: SupplierService) {}
  async ngOnInit() {
    await this.accountService.SessionInfo();
    await this.locationService.initLocations();
    await this.bookService.GetCategories({});
    await this.accountService.getRoles();
  }

}
