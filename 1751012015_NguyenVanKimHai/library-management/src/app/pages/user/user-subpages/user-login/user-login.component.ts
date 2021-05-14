import { ForgotPasswordModalComponent } from './../../../components/forgot-password-modal/forgot-password-modal.component';
import { ModalController } from './../../../../core/modal-controller/modal-controller.service';
import { Router } from '@angular/router';
import { FormBuilder } from '@angular/forms';
import {Component, OnDestroy, OnInit} from '@angular/core';
import { AccountService } from 'src/app/states/account-store/account.service';
import { AccountStore } from 'src/app/states/account-store/account.store';
import {ApiAccountService} from "../../../../API/api-account.service";
import {WebSocketService} from "../../../../services/web-socket.service";
import {Observable} from "rxjs";
import {AccountQuery} from "../../../../states/account-store/account.query";

@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['./user-login.component.scss']
})
export class UserLoginComponent implements OnInit, OnDestroy {
  loginGoogle$;
  loading = false;
  login_form = this.fb.group({
    user_name: [''],
    password: [''],
  })
  constructor(
    private fb: FormBuilder,
    private accountService: AccountService,
    private accountStore: AccountStore,
    private router: Router,
    private modalController: ModalController,
    private apiAccountService: ApiAccountService,
    private webSocketService: WebSocketService,
    private accountQuery: AccountQuery,
    ) { }

  async ngOnInit() {
    this.loginGoogle$ = this.webSocketService.listen('login-google').subscribe(async (res: any) => {
      if (res?.success) {
        this.accountStore.update({
          auth_info: res?.data,
        });
        localStorage.setItem('auth_info', JSON.stringify(this.accountQuery.getValue().auth_info));
        this.router.navigateByUrl("book-store/home");
      }
    });
    this.webSocketService.emit('join', {'auth_info': JSON.parse(localStorage.getItem('auth_info')), 'room': 0});
  }

  ngOnDestroy() {
    this.loginGoogle$.unsubscribe();
  }
  async Login() {
    try{
      let login_form_data = this.login_form.value
      const login_req = {
        user_name: login_form_data.user_name,
        password: login_form_data.password,
      }
      await this.accountService.Login(login_req);
      this.router.navigateByUrl('/book-store/home');
      toastr.success("Đăng nhập thành công");
    } catch(e) {
      toastr.error("Đăng nhập thất bại", e.msg || e.message)
    }
  }

  OpenForgotPasswordModal() {
    const modal = this.modalController.create({
      component: ForgotPasswordModalComponent,
      cssClass: 'modal-lg',
      componentProps: {
        role:"customer"
      },
    });
    modal.show().then();
    modal.onDismiss().then();
  }


  async loginGoogle() {
    const res = await this.apiAccountService.LoginGoogle();
    window.open(res?.url,"_blank");
  }
}
