import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'app-shop-header',
  templateUrl: './shop-header.component.html',
  styleUrls: ['./shop-header.component.scss']
})
export class ShopHeaderComponent implements OnInit {

  constructor(
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  onLogin(){
    this.router.navigateByUrl(`/user/login`);
  }
}
