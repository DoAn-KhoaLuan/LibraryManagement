import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiAppService {
  baseURL = "https://localhost:44323";
  constructor() { }

}
