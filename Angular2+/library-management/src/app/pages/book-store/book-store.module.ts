import { ShareComponentModule } from './../components/share-component.module';
import { BookStoreRoutingModule } from './book-store-routing.service';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BookStoreComponent } from './book-store.component';
import { FormsModule } from '@angular/forms';
import {ShopHeaderComponent} from "./components/shop-header/shop-header.component";
import {ShopFooterComponent} from "./components/shop-footer/shop-footer.component";
import { CheckoutComponent } from './components/checkout/checkout.component';
import { HomeComponent } from './components/home/home.component';
import { DetailComponent } from './components/detail/detail.component';
import {PipeModule} from "../../pipes/pipe/pipe.module";
import {RatingModule} from "ng-starrating";
import { SearchComponent } from './components/search/search.component';
import {BrowserModule} from "@angular/platform-browser";
import {NzCommentModule} from "ng-zorro-antd/comment";
import {NzAvatarModule} from "ng-zorro-antd/avatar";
import {ScrollingModule} from "@angular/cdk/scrolling";
import {NzIconModule} from "ng-zorro-antd/icon";
import {NzListModule} from "ng-zorro-antd/list";
import {NzFormModule} from "ng-zorro-antd/form";
import {NzButtonModule} from "ng-zorro-antd/button";

@NgModule({
  imports: [
    CommonModule,
    BookStoreRoutingModule,
    ShareComponentModule,
    FormsModule,
    PipeModule,
    RatingModule,
    NzCommentModule,
    NzAvatarModule,
    ScrollingModule,
    NzIconModule,
    NzListModule,
    NzFormModule,
    NzButtonModule
  ],
  declarations: [BookStoreComponent, ShopHeaderComponent, ShopFooterComponent, CheckoutComponent, HomeComponent, DetailComponent, SearchComponent],
  bootstrap:    [ BookStoreComponent, HomeComponent ]
})
export class BookStoreModule { }
