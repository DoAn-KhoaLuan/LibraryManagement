import { UserRegisterAccountComponent } from './pages/user/user-subpages/user-register-account/user-register-account.component';
import { LoginComponent } from './pages/admin/admin-subpages/login/login.component';
import { AdminModule } from './pages/admin/admin.module';
import { BookStoreComponent } from './pages/book-store/book-store.component';
import { UserComponent } from './pages/user/user.component';
import { AdminComponent } from './pages/admin/admin.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { UserLoginComponent } from './pages/user/user-subpages/user-login/user-login.component';


const routes: Routes = [
  { path: 'book-store',loadChildren: () => import('./pages/book-store/book-store.module').then(m => m.BookStoreModule)},
  { path: 'admin',  loadChildren: () => import('./pages/admin/admin.module').then(m => m.AdminModule)},
  { path: 'admin/login',   component: LoginComponent},

  { path: 'user',  loadChildren: () => import('./pages/user/user.module').then(m => m.UserModule)},
  { path: 'user/register',   component: UserRegisterAccountComponent},
  { path: 'user/login',   component: UserLoginComponent },
  { path: '', redirectTo: 'book-store',pathMatch: 'full'},
  { path: '**', redirectTo: 'book-store' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
