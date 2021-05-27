import {UtilService} from './../../../../services/util.service';
import {Router} from '@angular/router';
import {AccountService} from './../../../../states/account-store/account.service';
import {CustomerStore} from './../../../../states/customer-store/customer.store';
import {CustomerService} from './../../../../states/customer-store/customer.service';
import {Component, OnInit, ElementRef, ViewChild} from '@angular/core';
import {FormBuilder} from '@angular/forms';
import {combineLatest} from 'rxjs';
import {map, takeUntil} from 'rxjs/operators';
import {LocationQuery} from '../../../../states/location-store';
import { TelegramService } from 'src/app/services/telegram.service';

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
    email: '',
    phone: '',
    birthDate: '',
    gender: '',
  });

  locationForm = this.fb.group({
    provinceCode: '',
    districtCode: '',
    wardCode: '',
    address: '',
  });

  @ViewChild('passwordInput', {static: false}) passwordInput: ElementRef;

  constructor(
    private fb: FormBuilder,
    private customerService: CustomerService,
    private customerStore: CustomerStore,
    private accountService: AccountService,
    private locationQuery: LocationQuery,
    private router: Router,
    private util: UtilService,
    private telegramService: TelegramService
  ) {
  }

  provincesList$ = this.locationQuery.select('provincesList');
  districtsList$ = combineLatest([
    this.locationQuery.select('districtsList'),
    this.locationForm.controls['provinceCode'].valueChanges]).pipe(
    map(([districts, provinceCode]) => {
      if (!provinceCode) {
        return [];
      }
      return districts?.filter(dist => dist.province_code == provinceCode);
    })
  );
  wardsList$ = combineLatest([
    this.locationQuery.select('wardsList'),
    this.locationForm.controls['districtCode'].valueChanges]).pipe(
    map(([wards, districtCode]) => {
      if (!districtCode) {
        return [];
      }
      return wards?.filter(ward => ward.district_code == districtCode);
    })
  );

  ngOnInit() {
  }

  showPassword() {
    let elementPass = <HTMLInputElement> document.querySelector('#password');
    elementPass.type = 'text';
  }

  hidePassword() {
    let elementPass = <HTMLInputElement> document.querySelector('#password');
    elementPass.type = 'password';
  }

  displayMap = option => option && option.name || null;
  valueMap = option => option && option.code || null;

  async CreateCustomerAndAccount() {
    try {
      let form_data = this.userRegisterForm.value;
      let location_data = this.locationForm.value;

      if (form_data.password != form_data.confirmPassword) {
        return toastr.error('Tạo mới tài khoản thất bại', 'Mật khẩu nhập lại không chính xác');
      }
      if (!this.util.validatePhoneNumber(form_data.phone)) {
        return;
      }
      if (!this.util.validEmail(form_data.email)) {
        return;
      }

      const info_req = {
        account_name: form_data.userName || null,
        account_password: form_data.password || null,
        last_name: form_data.lastName || null,
        first_name: form_data.firstName || null,
        phone: form_data.phone || null,
        email: form_data.email || null,
        province_id: location_data.provinceCode || null,
        district_id: location_data.districtCode || null,
        ward_id: location_data.wardCode || null,
        birth_date: form_data.birthDate || null,
        address: form_data.address || null,
        role_id: 3,
      };

      let resp = await this.accountService.CreateAccountAndCustomer(info_req);
      const account = resp[0];
      const customer = resp[1];
      await this.telegramService.sendCreateCustomerAccount(account, customer);
      this.router.navigateByUrl('/user/login');
      toastr.success('Tạo mới tài khoản thành công');
    } catch (e) {
      toastr.error('Tạo mới tài khoản thất bại', e.msg || e.message);
    }
  }
}
