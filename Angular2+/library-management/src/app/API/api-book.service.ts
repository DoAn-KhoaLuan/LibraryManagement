import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { ApiAppService } from "./api-app.service";

@Injectable({
  providedIn: "root",
})
export class ApiBookService {
  baseURL: string;
  constructor(private http: HttpClient, private apiAppService: ApiAppService) {
    this.baseURL = this.apiAppService.baseURL;
  }
  async GetBooks(req) {
    return await this.http.post(this.baseURL+"/admin/book-management/get-books",req).toPromise();
  }

  async UpdateBook(req) {
    return await this.http.post(this.baseURL+"/admin/book-management/update-book",req).toPromise();
  }

  async CreateBook(req) {
    return await this.http.post(this.baseURL+"/admin/book-management/create-book",req).toPromise();
  }

  async DeleteBook(req) {
    return await this.http.post(this.baseURL+"/admin/book-management/delete-book",req).toPromise();
  }
}
