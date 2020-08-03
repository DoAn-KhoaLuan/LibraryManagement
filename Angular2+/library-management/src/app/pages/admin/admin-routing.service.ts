import { UserComponent } from './../user/user.component';
import { BookStoreComponent } from './../book-store/book-store.component';
import { AdminComponent } from './admin.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { SidebarMenuModule } from '../components/sidebar-menu/sidebar-menu.module';

const routes: Routes = [
    { path: '', component: AdminComponent, children: [
        { path: 'test', component: BookStoreComponent}//localhost:4200/admin/test
    ] 
    },//localhost:4200/admin/
    // { path: 'test', component: BookStoreComponent}//localhost:4200/admin/test
];
@NgModule({
    imports: [CommonModule, RouterModule.forChild(routes), ],
    exports: [RouterModule],
    declarations: [],
})
export class AdminRoutingModule { }
