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

const routes: Routes = [
    { path: '', component: AdminComponent, children: [
        { path: 'book-management', component: BookManagementComponent, children:[
            // { path: 'book-list',  },
            { path: 'create-book', component: CreateBookComponent}
        ]}
    ] 
    }
];
@NgModule({
    imports: [CommonModule, RouterModule.forChild(routes), FormsModule, MaterialModule],
    exports: [RouterModule, CreateBookComponent],
    declarations: [LoginComponent, CreateBookComponent],
})
export class AdminRoutingModule { }
