import { BookStoreRoutingModule } from './book-store-routing.service';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BookStoreComponent } from './book-store.component';

@NgModule({
  imports: [
    CommonModule,
    BookStoreRoutingModule
  ],
  declarations: [BookStoreComponent]
})
export class BookStoreModule { }
