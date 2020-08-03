import { SidebarMenuModule } from './../components/sidebar-menu/sidebar-menu.module';
import { AdminRoutingModule } from './admin-routing.service';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AdminComponent } from './admin.component';

@NgModule({
  imports: [
    CommonModule,
    AdminRoutingModule,
    SidebarMenuModule
  ],
  declarations: [AdminComponent]
})
export class AdminModule { }
