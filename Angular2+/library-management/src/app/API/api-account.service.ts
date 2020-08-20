import { HttpService } from './../services/http.service';
import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { ApiAppService } from "./api-app.service";

@Injectable({
  providedIn: "root",
})
export class ApiAccountService {
  baseURL: string;
  constructor(private http: HttpService, private apiAppService: ApiAppService) {
    this.baseURL = this.apiAppService.baseURL;
  }
  async GetAccounts(req) {
    return await this.http.post(this.baseURL+"/admin/account-management/get-accounts",req).toPromise();
  }

  async UpdateAccount(req) {
    return await this.http.post(this.baseURL+"/admin/account-management/update-account",req).toPromise();
  }

  async CreateAccount(req) {
    return await this.http.post(this.baseURL+"/admin/account-management/create-account",req).toPromise();
  }

  async DeleteAccount(req) {
    return await this.http.post(this.baseURL+"/admin/account-management/search-accounts",req).toPromise();
  }

  async SearchAccounts(req) {
    return await this.http.post(this.baseURL+"/admin/account-management/delete-account",req).toPromise();
  }

  async Login(req) {
    return await this.http.post(this.baseURL+"/admin/account-management/login",req).toPromise();
  }
}
