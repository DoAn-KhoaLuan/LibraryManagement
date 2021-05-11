import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {ApiOrderService} from "../../../../API/api-order.service";
import {AccountQuery} from "../../../../states/account-store/account.query";
import {FormBuilder} from "@angular/forms";
import {combineLatest} from "rxjs";
import {map} from "rxjs/operators";
import {LocationQuery} from "../../../../states/location-store";
import { TelegramService } from 'src/app/services/telegram.service';

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.scss']
})
export class CheckoutComponent implements OnInit {
  @ViewChild("paypalRef", {static: true}) private paypalRef: ElementRef;
  cartBooks = []
  total = 0.0;

  locationForm = this.fb.group({
    provinceCode: '',
    districtCode: '',
    wardCode: '',
    address: '',
  });
  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private apiOrderService: ApiOrderService,
    private router: Router,
    private auth: AccountQuery,
    private locationQuery: LocationQuery,
    private telegramService: TelegramService
  ) { }

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

  displayMap = option => option && option.name || null;
  valueMap = option => option && option.code || null;
  async ngOnInit() {
    this.cartBooks = JSON.parse(localStorage.getItem("order_details"));
    if (this.cartBooks?.length > 0) {
      this.cartBooks.forEach(detail => {
        this.total += detail.quantity * detail.book.retail_price
      })
    }
    window.paypal.Buttons({
      style: {
        layout: 'horizontal',
        color: 'blue',
        shape: 'rect',
        label: 'paypal'
      },
      createOrder: (data, actions) => {
        return actions.order.create({
          purchase_units: [
            {amount: {
                value: (this.total * 0.000042).toFixed(1),
                currency_code: 'USD',
                product_id: 12
              }
            }
          ]
        });
      },
      onApprove: async (data, actions) => {
        const res = await actions.order.capture();
        // TODO : check order.status == "success" => gọi api CreateOrder
        if (res.status === "COMPLETED" ) {
          await this.CreateOrder();
        }
      },

      onError: error => {
        console.log(error);
      }
    })
      .render(this.paypalRef.nativeElement);
  }

  async CreateOrder() {
    try {
      let total = 0.0;
      let order_lines = [];

      this.cartBooks.forEach(detail => {
        total += detail.quantity * detail.book.retail_price
        order_lines.push({
          book_id: detail.book.book_id,
          quantity: detail.quantity
        })
      })

      const create_order_req = {
        customer_id:  this.auth.getValue().auth_info?.user_info?.customer_id || 1,
        order_date: Date.now(),
        type: 'online',
        total: parseInt(total.toFixed(0)),
        order_detail_list: order_lines
      };
      await this.apiOrderService.CreateOrder(create_order_req).then(async order =>  {
        await this.telegramService.sendCreateOrder(order)
        toastr.success('Thanh toán hóa đơn thành công');
        this.router.navigateByUrl("/book-store/home")
        localStorage.removeItem("order_details")
      });

    } catch (e) {
      toastr.error('Thanh toán hóa đơn thất bại');
    }
  }

  async CreateOrderByMomo() {
    try {
      const customer_id = this.auth.getValue().auth_info?.user_info?.customer_id;
      let order_lines = [];

      this.cartBooks.forEach(detail => {
        order_lines.push({
          book_id: detail.book.book_id,
          quantity: detail.quantity
        })
      })
      const create_order_req = {
        customer_id: customer_id || 1,
        type:'online',
        total: this.total.toFixed(0),
        order_detail_list: order_lines
      }
      let result = await this.apiOrderService.CreateOrderByMoMo(create_order_req)
      if (result.errorCode === 0) {
        toastr.success('Thanh toán hóa đơn bằng MOMO thành công')
        localStorage.removeItem("order_details")
        window.location.href = result.payUrl
      }
    } catch (e) {
      toastr.error('Thanh toán hóa đơn bằng MOMO thất bại')
    }
  }

  changeQuantity() {
    this.total = 0.0;
    this.cartBooks.forEach(detail => {
      detail.quantity = parseInt(detail.quantity)
      this.total += detail.quantity * detail.book.retail_price
    })
    localStorage.setItem("order_details", JSON.stringify(this.cartBooks));
  }

  increaseQuantity(order_detail, type: string) {
    if (type == "increase") {
      order_detail.quantity =  parseInt(order_detail.quantity) + 1;
    }
    if (type == "decrease") {
      if (order_detail.quantity == 1 ) {
        return toastr.error("Thao tác không thành công")
      }
      order_detail.quantity =  parseInt(order_detail.quantity) - 1;
    }
    if (type == "delete") {
      this.cartBooks = this.cartBooks.filter(detail => {
        return detail.book.book_id != order_detail.book.book_id
      })
    }
      this.changeQuantity()
  }
}
