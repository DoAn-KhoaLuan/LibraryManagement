import { ResetPasswordComponent } from './pages/components/reset-password/reset-password.component';
import { LoginViewGuard } from './login.guard';
import { UserRegisterAccountComponent } from './pages/user/user-subpages/user-register-account/user-register-account.component';
import { LoginComponent } from './pages/admin/admin-subpages/login/login.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { UserLoginComponent } from './pages/user/user-subpages/user-login/user-login.component';
import { AuthGuard } from './auth-guard';


const routes: Routes = [
  { path: 'book-store',loadChildren: () => import('./pages/book-store/book-store.module').then(m => m.BookStoreModule)},
  { path: 'admin', loadChildren: () => import('./pages/admin/admin.module').then(m => m.AdminModule)},
  { path: 'admin/login', component: LoginComponent},

  { path: 'user',  loadChildren: () => import('./pages/user/user.module').then(m => m.UserModule)},
  { path: 'user/register',   component: UserRegisterAccountComponent},
  { path: 'user/login',   component: UserLoginComponent },
  { path: 'reset-password', component: ResetPasswordComponent},
  { path: '', redirectTo: 'book-store',pathMatch: 'full'},
  { path: '**', redirectTo: 'book-store' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  declarations: [],
})
export class AppRoutingModule { }
