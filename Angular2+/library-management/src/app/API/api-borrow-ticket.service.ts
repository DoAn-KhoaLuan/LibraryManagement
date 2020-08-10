import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { ApiAppService } from "./api-app.service";

@Injectable({
  providedIn: "root",
})
export class ApiBorrowTicketService {
  baseURL: string;
  constructor(private http: HttpClient, private apiAppService: ApiAppService) {
    this.baseURL = this.apiAppService.baseURL;
  }
  async GetBorrowTickets(req) {
    return await this.http.post(this.baseURL+"/admin/borrow-ticket-management/get-borrow-tickets",req).toPromise();
  }

  async UpdateBorrowTicket(req) {
    return await this.http.post(this.baseURL+"/admin/borrow-ticket-management/update-borrow-ticket",req).toPromise();
  }

  async CreateBorrowTicket(req) {
    return await this.http.post(this.baseURL+"/admin/borrow-ticket-management/create-borrow-ticket",req).toPromise();
  }

  async DeleteBorrowTicket(req) {
    return await this.http.post(this.baseURL+"/admin/borrow-ticket-management/delete-borrow-ticket",req).toPromise();
  }
}
