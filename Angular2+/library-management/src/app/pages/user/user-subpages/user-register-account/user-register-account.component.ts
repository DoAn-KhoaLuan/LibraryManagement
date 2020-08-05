import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-user-register-account',
  templateUrl: './user-register-account.component.html',
  styleUrls: ['./user-register-account.component.scss']
})
export class UserRegisterAccountComponent implements OnInit {
  loading = false;
  userRegisterForm = this.fb.group({
    userName: [''],
    password: [''],
    confirmPassword: [''],
    firstName: '',
    lastName: '',
    identityId: '',
    email:'',
    phone: '',
    birthDate: '',
    address: '',
    gender: '',
  })

  @ViewChild('passwordInput', {static: false}) passwordInput: ElementRef;

  constructor(private fb: FormBuilder) { }

  ngOnInit() {
    this.userRegisterForm.valueChanges.subscribe(val => console.log(val))
  }

  
  showPassword() {
    let elementPass = <HTMLInputElement>document.querySelector('#password');
    elementPass.type = 'text';
  }

  hidePassword() {
    let elementPass = <HTMLInputElement>document.querySelector('#password');
    elementPass.type = 'password';
  }
}
