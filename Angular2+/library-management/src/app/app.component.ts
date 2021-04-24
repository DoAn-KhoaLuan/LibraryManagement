import { AccountService } from './states/account-store/account.service';
import {Component, OnInit} from '@angular/core';
import {BookService} from "./states/book-store/book.service";
import {ApiAccountService} from "./API/api-account.service";
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  loadingPage = false;
  constructor(private accountService: AccountService,
              private bookService: BookService,
              private apiAccountService: ApiAccountService
              ) {
  }
  async ngOnInit() {
    await this.bookService.GetCategories({}).then();
    this.apiAccountService.getProvinces();
    this.apiAccountService.getDistricts();
    this.apiAccountService.getWards();
  }

}
