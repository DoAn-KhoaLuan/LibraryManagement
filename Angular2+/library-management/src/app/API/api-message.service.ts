import {Injectable} from "@angular/core";
import {HttpService} from "../services/http.service";
import {ApiAppService} from "./api-app.service";

@Injectable({
  providedIn: "root",
})
export class ApiMessageService {
  baseURL: string;
  constructor(private http: HttpService, private apiAppService: ApiAppService) {
    this.baseURL = this.apiAppService.baseURL;
  }
  async GetMessages(req) {
    return await this.http.post(this.baseURL+"/message/get-messages",req).toPromise();
  }

  async SendMessage(req) {
    return await this.http.post(this.baseURL+"/message/send-message",req).toPromise();
  }

  async GetConversationByCustomerAccountId(req) {
    return await this.http.post(this.baseURL+"/message/get-conversation-by-customer-account-id",req).toPromise();
  }
}
