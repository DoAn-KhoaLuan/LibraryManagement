import { ShareComponentModule } from './../components/share-component.module';
import { BookStoreRoutingModule } from './book-store-routing.service';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BookStoreComponent } from './book-store.component';
import { FormsModule } from '@angular/forms';
import {ShopHeaderComponent} from "./components/shop-header/shop-header.component";
import {ShopFooterComponent} from "./components/shop-footer/shop-footer.component";

@NgModule({
  imports: [
    CommonModule,
    BookStoreRoutingModule,
    ShareComponentModule,
    FormsModule
  ],
  declarations: [BookStoreComponent, ShopHeaderComponent, ShopFooterComponent]
})
export class BookStoreModule { }
