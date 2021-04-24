import { AccountService } from '../../../../../../states/account-store/account.service';
import { AccountStore } from '../../../../../../states/account-store/account.store';
import { AccountQuery } from '../../../../../../states/account-store/account.query';
import { Router } from '@angular/router';
import { PaginationOpt } from '../../../../../../shared/page-pagination/page-pagination.component';
import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import {FormBuilder} from "@angular/forms";

@Component({
  selector: 'app-account-list',
  templateUrl: './account-list.component.html',
  styleUrls: ['./account-list.component.scss']
})
export class AccountListComponent implements OnInit {
  account_list$ = this.accountQuery.account_list_view$;
  current_pagination_opt$ = this.accountQuery.current_pagination_opt$;
  current_page$ = this.accountQuery.current_page$;
  roles$ = this.accountQuery.roles$;
  currentPaginationOpt = new PaginationOpt();

  searchForm = this.fb.group({
    role_id: '',
    account_id: '',
    account_name: '',
  });

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private ref: ChangeDetectorRef,
    private accountQuery: AccountQuery,
    private accountStore: AccountStore,
    private accountService: AccountService) { }

  async ngOnInit() {
    await this.onRequestNewPage();
  }

  async onRequestNewPage() {
    await this.accountService.GetAccounts(this.accountQuery.getValue().filter_page).then(() => {
      this.accountService.setupPagination();
    })
  }

  async navigate(direction) {
    this.accountService.navigate(direction);
    await this.onRequestNewPage()
  }

  onViewAccountDetail(account_id) {
    this.router.navigateByUrl(`/admin/account-management/account-detail/${account_id}`);
  }

  async search() {
    let {
      account_id,
      account_name,
      role_id
    } = this.searchForm.value;
    if (!account_id && !account_name && !role_id) {
      return await this.onRequestNewPage();
    }
    const req = {
        account_id: account_id || null,
        account_name: account_name || null,
        role_id: role_id || null
    };
    let accounts = await this.accountService.SearchAccounts(req);
    this.accountStore.update({
      account_list_view: {
        items: accounts,
        has_next: false,
        has_prev: false,
        current_page: 1
      }
    });
  }
}
