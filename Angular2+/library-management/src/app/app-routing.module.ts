import { AdminModule } from './pages/admin/admin.module';
import { BookStoreComponent } from './pages/book-store/book-store.component';
import { UserComponent } from './pages/user/user.component';
import { AdminComponent } from './pages/admin/admin.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';


const routes: Routes = [
  { path: 'book-store',loadChildren: () => import('./pages/book-store/book-store.module').then(m => m.BookStoreModule)},
  { path: 'admin',  loadChildren: () => import('./pages/admin/admin.module').then(m => m.AdminModule)},
  { path: 'user',  loadChildren: () => import('./pages/user/user.module').then(m => m.UserModule)},
  { path: '', redirectTo: 'book-store',pathMatch: 'full'},
  { path: '**', redirectTo: 'book-store' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
