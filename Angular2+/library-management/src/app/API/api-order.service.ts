import { HttpService } from './../services/http.service';
import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { ApiAppService } from "./api-app.service";

@Injectable({
  providedIn: "root",
})
export class ApiOrderService {
  baseURL: string;
  constructor(private http: HttpService, private apiAppService: ApiAppService) {
    this.baseURL = this.apiAppService.baseURL;
  }
  async GetOrders(req) {
    return await this.http.post(this.baseURL+"/admin/order-management/get-orders",req).toPromise();
  }

  async UpdateOrder(req) {
    return await this.http.post(this.baseURL+"/admin/order-management/update-order",req).toPromise();
  }

  async CreateOrder(req) {
    return await this.http.post(this.baseURL+"/admin/order-management/create-order",req).toPromise();
  }

  async DeleteOrder(req) {
    return await this.http.post(this.baseURL+"/admin/order-management/delete-order",req).toPromise();
  }
}
