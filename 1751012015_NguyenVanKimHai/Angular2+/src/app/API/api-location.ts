import {Injectable} from '@angular/core';
import {HttpService} from '../services/http.service';

@Injectable({
  providedIn: 'root'
})
export class ApiLocation {

  baseUrl: string;
  constructor(
    private http: HttpService
  ) {
    this.baseUrl = 'https://shop.d.etop.vn';
  }



  listProvinces() {
    return this.http.post(this.baseUrl + '/api/etop.Location/GetProvinces', {}).toPromise();
  }

  listDistricts() {
    return this.http.post(this.baseUrl + '/api/etop.Location/GetDistricts', {}).toPromise();
  }

  listWards() {
    return this.http.post(this.baseUrl + '/api/etop.Location/GetWards', {}).toPromise();
  }

}
