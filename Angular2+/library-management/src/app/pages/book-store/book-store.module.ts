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

@NgModule({
  imports: [
    CommonModule,
    BookStoreRoutingModule,
    ShareComponentModule,
    FormsModule,
    PipeModule,
    RatingModule
  ],
  declarations: [BookStoreComponent, ShopHeaderComponent, ShopFooterComponent, CheckoutComponent, HomeComponent, DetailComponent, SearchComponent],
  bootstrap:    [ BookStoreComponent, HomeComponent ]
})
export class BookStoreModule { }
