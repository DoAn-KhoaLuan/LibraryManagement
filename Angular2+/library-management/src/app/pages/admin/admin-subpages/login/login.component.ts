import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  account :any ={};
  loading = false;
 
  @ViewChild('passwordInput', {static: false}) passwordInput: ElementRef;

  constructor() { }

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
}
