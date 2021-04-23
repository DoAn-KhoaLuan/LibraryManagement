import { HttpService } from './../services/http.service';
import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { ApiAppService } from "./api-app.service";

@Injectable({
  providedIn: "root",
})
export class ApiProductService {
  baseURL: string;
  constructor(private http: HttpService, private apiAppService: ApiAppService) {
    this.baseURL = this.apiAppService.baseURL;
  }

  async GetCategories() {
    return await this.http.post(this.baseURL+"get-categories",{}).toPromise();
  }
  async GetProductsByShop(req) {
    return await this.http.post(this.baseURL+"/admin/product-management/get-products-by-shop",req).toPromise();
  }

  async SearchShopProduct(req) {
    return await this.http.post(this.baseURL+"/admin/product-management/search-shop-products",req).toPromise();
  }

  async UpdateProduct(req) {
    return await this.http.post(this.baseURL+"/admin/product-management/update-product  ",req).toPromise();
  }

  async CreateProduct(req) {
    return await this.http.post(this.baseURL+"/admin/product-management/create-product",req).toPromise();
  }

  async GetShopProductById(req) {
    return await this.http.post(this.baseURL+"/admin/product-management/get-shop-product-by-id",req).toPromise();
  }

  async DeleteProduct(req) {
    return await this.http.post(this.baseURL+"/admin/product-management/delete-product",req).toPromise();
  }

  async UploadImage(imageForm, opt) {
    return await this.http.post(this.baseURL+"/upload-image",imageForm, opt).toPromise();
  }
}
