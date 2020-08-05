import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { MaterialModule } from './../../shared/material.module';
import { BookManagementComponent } from './admin-subpages/book-management/book-management.component';
import { SidebarMenuModule } from './../components/sidebar-menu/sidebar-menu.module';
import { AdminRoutingModule } from './admin-routing.service';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AdminComponent } from './admin.component';

@NgModule({
  imports: [
    CommonModule,
    AdminRoutingModule,
    SidebarMenuModule, 
    MaterialModule,

  ],
  declarations: [AdminComponent, BookManagementComponent],
  exports: [BookManagementComponent]
})
export class AdminModule { }
