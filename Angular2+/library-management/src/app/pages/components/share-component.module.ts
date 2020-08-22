import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ForgotPasswordModalComponent } from './forgot-password-modal/forgot-password-modal.component';
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
@NgModule({
    imports: [
      CommonModule,
      FormsModule,
      ReactiveFormsModule

    ],
    declarations: [
        ForgotPasswordModalComponent,
        ResetPasswordComponent
    ],
    exports: [
        ForgotPasswordModalComponent,
        ResetPasswordComponent
    ],
  })
  export class ShareComponentModule { }