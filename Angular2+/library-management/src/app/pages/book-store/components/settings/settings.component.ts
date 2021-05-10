import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { combineLatest } from 'rxjs';
import { map } from 'rxjs/operators';
import { CustomerService } from 'src/app/states/customer-store/customer.service';
import { LocationQuery } from 'src/app/states/location-store';
import { OrderQuery } from 'src/app/states/order-store/order.query';
import { OrderService } from 'src/app/states/order-store/order.service';
import { OrderStore } from 'src/app/states/order-store/order.store';
import {AccountQuery} from '../../../../states/account-store/account.query';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.scss']
})
export class SettingsComponent implements OnInit {
  view: "order" | "customer_info" = "customer_info";
  item_list = [
    {
      title: "Thông tin tài khoản",
      icon: "fas fa-user fa",
      view: "customer_info"
    },
    {
      title: "Đơn hàng của tôi",
      icon: "fas fa-file-invoice-dollar",
      view: "order"
    },
  ]
  initProvince = true;
  datetime;
  auth_info;
  locationForm = this.fb.group({
    provinceCode: '',
    districtCode: '',
    wardCode: '',
    address: '',
  });

  order_list$ = this.orderQuery.order_list_view$;
  constructor(
    private fb: FormBuilder,
    private accountQuery: AccountQuery,
    private locationQuery: LocationQuery,
    private datePipe: DatePipe,
    private customerService: CustomerService,
    private orderService: OrderService,
    private orderStore: OrderStore,
    private orderQuery: OrderQuery
  ) { }
  

  provincesList$ = this.locationQuery.select('provincesList');
  districtsList$ = combineLatest([
    this.locationQuery.select('districtsList'),
    this.locationForm.controls['provinceCode'].valueChanges]).pipe(
    map(([districts, provinceCode]) => {
      if (!provinceCode ) {
        return [];
      }
      if (this.initProvince) {
        this.locationForm.patchValue({
          districtCode: this.auth_info.user_info.district_id,
        })
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

  displayMap = option => option && option.name || null;
  valueMap = option => option && option.code || null;
  async ngOnInit() {
    this.auth_info = this.accountQuery.getValue().auth_info;
    this.auth_info.user_info.birth_day = this.datePipe.transform(this.auth_info.user_info.birth_day, 'yyyy-MM-dd')
    console.log(this.auth_info);
    console.log(this.auth_info.user_info.birth_day);
    this.locationForm.patchValue({
      provinceCode: this.auth_info.user_info.province_id,
      districtCode: this.auth_info.user_info.district_id,
      wardCode: this.auth_info.user_info.ward_id,
      address: this.auth_info.user_info.address,
    })
    await this.search();
  }

  async UpdateUser() {
    try {
      const user_info = this.auth_info.user_info;
      const form_data = this.locationForm.getRawValue();
      if(user_info.account.role.role_id == 3) { // nếu là customer
        const update_info_req = {
          account_id: user_info.account.account_id,
          customer_id: user_info.customer_id,
          last_name: user_info.last_name,
          first_name: user_info.first_name,
          birth_date: user_info.birth_day,
          gender: user_info.gender == "true" ? true : false,
          address: form_data.address,
          note: user_info.note,
          image: user_info.image,
          email: user_info.email,
          identity_id: user_info.identity_id,
          phone: user_info.phone,
          province_id: form_data.provinceCode,
          district_id: form_data.districtCode,
          ward_id: form_data.wardCode,
        }
        await this.customerService.UpdateCustomer(update_info_req)
      }

      toastr.success("Cập nhật thông tin cá nhân thành công");
    } catch(e) {
      toastr.error("Cập nhật thông tin cá nhân không thành công", e.msg || e.message)
    }
  }

  async search() {
    const user_info = this.auth_info.user_info;
    const req = {
      customer_id: user_info.customer_id
    };
    let orders = await this.orderService.searchOrders(req);
    this.orderStore.update({
      order_list_view: {
        items: orders,
        has_next: false,
        has_prev: false,
        current_page: 1
      }
    });
  }
  changeView(view) {
    this.view = view;
  }
}
