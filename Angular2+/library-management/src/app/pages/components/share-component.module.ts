import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ForgotPasswordModalComponent } from './forgot-password-modal/forgot-password-modal.component';
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import {DashboardBoxComponent} from "./dashboard-box/dashboard-box.component";
@NgModule({
    imports: [
      CommonModule,
      FormsModule,
      ReactiveFormsModule

    ],
    declarations: [
        ForgotPasswordModalComponent,
        ResetPasswordComponent,
        DashboardBoxComponent
    ],
    exports: [
        ForgotPasswordModalComponent,
        ResetPasswordComponent,
        DashboardBoxComponent
    ],
  })
  export class ShareComponentModule { }
