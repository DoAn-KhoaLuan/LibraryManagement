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

const routes: Routes = [
    { path: '', component: AdminComponent, children: [
        { path: 'book-management', component: BookManagementComponent, children:[
            { path: 'create-book', component: CreateBookComponent},
            { path: 'book-list', component: BookListComponent},
            { path: 'book-detail/:id', component: BookDetailComponent},
        ]}
    ] 
    }
];
@NgModule({
    imports: [CommonModule, RouterModule.forChild(routes), FormsModule, MaterialModule, ItemTableModule,MatInputModule, PaginationModule, PipeModule],
    exports: [RouterModule, CreateBookComponent, AddSupplierModalComponent, AddAuthorModalComponent, AddCategoryModalComponent],
    declarations: [LoginComponent, CreateBookComponent, AddSupplierModalComponent, AddCategoryModalComponent, BookListComponent, BookRowComponent, BookDetailComponent, ConfirmDeleteModalComponent, AddAuthorModalComponent],
})
export class AdminRoutingModule { }
