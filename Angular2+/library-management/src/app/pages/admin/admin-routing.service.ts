import { CreateSupplierComponent } from './admin-subpages/supplier-management/components/create-supplier/create-supplier.component';
import { SupplierRowComponent } from './admin-subpages/supplier-management/components/supplier-list/supplier-row/supplier-row.component';
import { SupplierListComponent } from './admin-subpages/supplier-management/components/supplier-list/supplier-list.component';
import { EmployeeDetailComponent } from './admin-subpages/employee-management/components/employee-detail/employee-detail.component';
import { EmployeeListComponent } from './admin-subpages/employee-management/components/employee-list/employee-list.component';
import { ConfirmDeleteCustomerComponent } from './admin-subpages/customer-management/components/customer-detail/confirm-delete-customer/confirm-delete-customer.component';
import { CustomerDetailComponent } from './admin-subpages/customer-management/components/customer-detail/customer-detail.component';

import { CustomerManagementComponent } from './admin-subpages/customer-management/customer-management.component';
import { ConfirmDeleteModalComponent } from './admin-subpages/book-management/components/book-detail/confirm-delete-modal/confirm-delete-modal.component';
import { PipeModule } from 'src/app/pipes/pipe/pipe.module';
import { BookDetailComponent } from './admin-subpages/book-management/components/book-detail/book-detail.component';
import { PaginationModule } from './../../shared/page-pagination/page-pagination.module';
import { MatInputModule } from './../../shared/mat-input/mat-input.module';
import { ItemTableComponent } from './../components/item-table/item-table.component';
import { BookListComponent } from './admin-subpages/book-management/components/book-list/book-list.component';
import { MaterialModule } from './../../shared/material.module';
import { FormsModule } from '@angular/forms';
import { CreateBookComponent } from './admin-subpages/book-management/components/create-book/create-book.component';
import { BookManagementComponent } from './admin-subpages/book-management/book-management.component';
import { BookStoreComponent } from './../book-store/book-store.component';
import { LoginComponent } from './admin-subpages/login/login.component';
import { AdminComponent } from './admin.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { ItemTableModule } from '../components/item-table/item-table.module';
import { BookRowComponent } from './admin-subpages/book-management/components/book-list/book-row/book-row.component';
import { AddAuthorModalComponent } from './admin-subpages/book-management/components/add-author-modal/add-author-modal.component';
import { AddCategoryModalComponent } from './admin-subpages/book-management/components/add-category-modal/add-category-modal.component';
import { AddSupplierModalComponent } from './admin-subpages/book-management/components/add-supplier-modal/add-supplier-modal.component';
import { AuthGuard } from 'src/app/auth-guard';
import { CustomerListComponent } from './admin-subpages/customer-management/components/customer-list/customer-list.component';
import { CustomerRowComponent } from './admin-subpages/customer-management/components/customer-list/customer-row/customer-row.component';
import { EmployeeManagementComponent } from './admin-subpages/employee-management/employee-management.component';
import { EmployeeRowComponent } from './admin-subpages/employee-management/components/employee-list/employee-row/employee-row.component';
import { ConfirmDeleteEmployeeComponent } from './admin-subpages/employee-management/components/employee-detail/confirm-delete-employee/confirm-delete-employee.component';
import { SupplierManagementComponent } from './admin-subpages/supplier-management/supplier-management.component';
import { SupplierDetailComponent } from './admin-subpages/supplier-management/components/supplier-detail/supplier-detail.component';

const routes: Routes = [
    { path: '', component: AdminComponent, children: [
        { path: 'book-management', component: BookManagementComponent, children:[
            { path: 'create-book', component: CreateBookComponent},
            { path: 'book-list', component: BookListComponent},
            { path: 'book-detail/:id', component: BookDetailComponent},
            { path: '', redirectTo: 'book-list',pathMatch: 'full'},
            { path: '**', redirectTo: 'book-list' },
        ]},
        { path: 'customer-management', component: CustomerManagementComponent, children:[
            { path: 'customer-list', component: CustomerListComponent},
            { path: 'customer-detail/:id', component: CustomerDetailComponent},
            { path: '', redirectTo: 'customer-list',pathMatch: 'full'},
            { path: '**', redirectTo: 'customer-list' },
        ]},
        { path: 'employee-management', component: EmployeeManagementComponent, children:[
            { path: 'employee-list', component: EmployeeListComponent},
            { path: 'employee-detail/:id', component: EmployeeDetailComponent},
            { path: '', redirectTo: 'employee-list',pathMatch: 'full'},
            { path: '**', redirectTo: 'employee-list' },
        ]},
        { path: 'supplier-management', component: SupplierManagementComponent, children:[
            { path: 'create-supplier', component: CreateSupplierComponent},
            { path: 'supplier-list', component: SupplierListComponent},
            { path: 'supplier-detail/:id', component: SupplierDetailComponent},
            { path: '', redirectTo: 'supplier-list',pathMatch: 'full'},
            { path: '**', redirectTo: 'supplier-list' },
        ]},
        { path: '', redirectTo: 'book-management',pathMatch: 'full'},
        { path: '**', redirectTo: 'book-management' },
    ] 
    }
];
@NgModule({
    imports: [CommonModule, RouterModule.forChild(routes), FormsModule, MaterialModule, ItemTableModule,MatInputModule, PaginationModule, PipeModule],
    exports: [RouterModule, CreateBookComponent, AddSupplierModalComponent, AddAuthorModalComponent, AddCategoryModalComponent],
    declarations: [LoginComponent, CreateBookComponent, AddSupplierModalComponent, AddCategoryModalComponent, BookListComponent, BookRowComponent, BookDetailComponent, ConfirmDeleteModalComponent, AddAuthorModalComponent, CustomerListComponent, CustomerManagementComponent, CustomerRowComponent, CustomerDetailComponent, ConfirmDeleteCustomerComponent, EmployeeManagementComponent, EmployeeListComponent, EmployeeRowComponent, EmployeeDetailComponent, ConfirmDeleteEmployeeComponent, SupplierListComponent, SupplierRowComponent,SupplierManagementComponent, SupplierDetailComponent, CreateSupplierComponent],
})
export class AdminRoutingModule { }
