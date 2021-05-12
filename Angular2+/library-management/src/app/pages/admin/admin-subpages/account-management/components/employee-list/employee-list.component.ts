import { EmployeeService } from '../../../../../../states/employee-store/employee.service';
import { EmployeeStore } from '../../../../../../states/employee-store/employee.store';
import { EmployeeQuery } from '../../../../../../states/employee-store/employee.query';
import { Router } from '@angular/router';
import { PaginationOpt } from '../../../../../../shared/page-pagination/page-pagination.component';
import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import {FormBuilder} from "@angular/forms";

@Component({
  selector: 'app-employee-list',
  templateUrl: './employee-list.component.html',
  styleUrls: ['./employee-list.component.scss']
})
export class EmployeeListComponent implements OnInit {
  employee_list$ = this.employeeQuery.employee_list_view$;
  current_pagination_opt$ = this.employeeQuery.current_pagination_opt$;
  current_page$ = this.employeeQuery.current_page$;
  currentPaginationOpt = new PaginationOpt();
  searchForm = this.fb.group({
    employee_id: '',
    phone: '',
  });
  constructor(
    private fb: FormBuilder,
    private router: Router,
    private ref: ChangeDetectorRef,
    private employeeQuery: EmployeeQuery,
    private employeeStore: EmployeeStore,
    private employeeService: EmployeeService) { }

  async ngOnInit() {
    await this.onRequestNewPage();
  }

  async onRequestNewPage() {
    await this.employeeService.GetEmployees(this.employeeQuery.getValue().filter_page).then(() => {
      this.employeeService.setupPagination();
    })
  }

  async navigate(direction) {
    this.employeeService.navigate(direction);
    await this.onRequestNewPage()
  }

  onViewEmployeeDetail(employee_id) {
    this.router.navigateByUrl(`/admin/account-management/employee-detail/${employee_id}`);
  }

  async search() {
    let {
      employee_id,
      phone,
    } = this.searchForm.value;
    if (!employee_id && !phone) {
      return await this.onRequestNewPage();
    }
    const req = {
      employee_id: employee_id || null,
      phone: phone || null,
    };
    let employees = await this.employeeService.SearchEmployees(req);
    this.employeeStore.update({
      employee_list_view: {
        items: employees,
        has_next: false,
        has_prev: false,
        current_page: 1
      }
    });
  }

}
