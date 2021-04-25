import { async } from '@angular/core/testing';
import { SupplierStore } from '../../../../../../states/supplier-store/supplier.store';
import { SupplierQuery } from '../../../../../../states/supplier-store/supplier.query';
import { SupplierService } from '../../../../../../states/supplier-store/supplier.service';
import { Router } from '@angular/router';
import { PaginationOpt, NavigationDirection } from '../../../../../../shared/page-pagination/page-pagination.component';
import { Subject } from 'rxjs';
import { ApiSupplierService } from '../../../../../../API/api-supplier.service';
import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import {FormBuilder} from "@angular/forms";

@Component({
  selector: 'app-supplier-list',
  templateUrl: './supplier-list.component.html',
  styleUrls: ['./supplier-list.component.scss']
})
export class SupplierListComponent implements OnInit {
  supplier_list$ = this.supplierQuery.supplier_list_view$;
  current_pagination_opt$ = this.supplierQuery.current_pagination_opt$;
  current_page$ = this.supplierQuery.current_page$;
  currentPaginationOpt = new PaginationOpt();

  searchForm = this.fb.group({
    supplier_id: '',
    supplier_name: '',
    email: '',
  });

  constructor(
    private fb: FormBuilder,
    private router: Router, private supplierService: SupplierService, private supplierQuery: SupplierQuery, private supplierStore: SupplierStore, private ref: ChangeDetectorRef) { }

  async ngOnInit() {
    await this.onRequestNewPage();
  }

  async onRequestNewPage() {
    await this.supplierService.GetSuppliers(this.supplierQuery.getValue().filter_page).then(() => {
      this.supplierService.setupPagination();
    })
  }

  async navigate(direction) {
    this.supplierService.navigate(direction);
    await this.onRequestNewPage()
  }

  onViewSupplierDetail(supplier_id) {
    this.router.navigateByUrl(`/admin/supplier-management/supplier-detail/${supplier_id}`);
  }


  async search() {
    let {
      supplier_id,
      supplier_name,
      email
    } = this.searchForm.value;
    if (!supplier_id && !supplier_name && !email) {
      return await this.onRequestNewPage();
    }
    const req = {
      supplier_id: supplier_id || null,
      contact_name: supplier_name || null,
      email: email || null
    };
    let suppliers = await this.supplierService.SearchSuppliers(req);
    this.supplierStore.update({
      supplier_list_view: {
        items: suppliers,
        has_next: false,
        has_prev: false,
        current_page: 1
      }
    });
  }
}
