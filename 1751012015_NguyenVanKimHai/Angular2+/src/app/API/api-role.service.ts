import { HttpService } from './../services/http.service';
import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { ApiAppService } from "./api-app.service";

@Injectable({
  providedIn: "root",
})
export class ApiRoleService {
  baseURL: string;
  constructor(private http: HttpService, private apiAppService: ApiAppService) {
    this.baseURL = this.apiAppService.baseURL;
  }
  mapDisplayName = {
    "admin": "Người quản trị",
    "admin-manager": "Nhân viên quản lý",
    "user": "Quản lý",
  }

  async GetRoles() {
    return await this.http.post(this.baseURL+"/admin/role-management/get-roles", {}).toPromise().then(roles => roles.map(role => {
      const display_name = this.mapDisplayName[role?.role_name] || role?.role_name;
      return {
        ...role,
        display_name: display_name
      };
    }));
  }

  async UpdateRole(req) {
    return await this.http.post(this.baseURL+"/admin/role-management/update-role",req).toPromise();
  }

  async CreateRole(req) {
    return await this.http.post(this.baseURL+"/admin/role-management/create-role",req).toPromise();
  }

  async DeleteRole(req) {
    return await this.http.post(this.baseURL+"/admin/role-management/delete-role",req).toPromise();
  }
}
