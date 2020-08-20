import { Router } from '@angular/router';
import { FormBuilder } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { AccountService } from 'src/app/states/account-store/account.service';
import { AccountStore } from 'src/app/states/account-store/account.store';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  account :any ={};
  loading = false;
 
  login_form = this.fb.group({
    user_name: [''],
    password: [''],
  })
  constructor(
    private fb: FormBuilder,
    private accountService: AccountService,
    private accountStore: AccountStore,
    private router: Router
  ) { }

  ngOnInit() {
  }

  showPassword() {
    let elementPass = <HTMLInputElement>document.querySelector('#password');
    elementPass.type = 'text';
  }

  hidePassword() {
    let elementPass = <HTMLInputElement>document.querySelector('#password');
    elementPass.type = 'password';
  }
  
  async onLogin() {
    // let res;
    // this.loading = true;
    // try {
    //   if(!this.account.userName  || !this.account.password){
    //     throw new Error("Vui lòng nhập đầy đủ thông tin tài khoản !")
    //   }
    //   res = await this.authService.login(this.account);
    //   if(res.success) {
    //     toastr.success(res.message);
    //     this.router.navigateByUrl("/admin/book-management");
    //   } else {
    //     toastr.error(res.message);
    //   }
    // } 
    // catch(e) {
    //   toastr.error(e.message, "Đăng nhập thất bại");
    //   this.loading = false;
    // }
    // this.loading = false;
  }
  async Login() {
    try{
      let login_form_data = this.login_form.value
      const login_req = {
        user_name: login_form_data.user_name,
        password: login_form_data.password,
      }
      await this.accountService.Login(login_req)
      this.router.navigateByUrl('admin/book-management/book-list')
      toastr.success("Đăng nhập thành công")
    } catch(e) {
      toastr.error("Đăng nhập thất bại", e.msg || e.message)
    }
  }
}
