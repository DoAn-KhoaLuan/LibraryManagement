import { Router } from '@angular/router';
import { ApiBookService } from './../../../../../../API/api-book.service';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-book-detail',
  templateUrl: './book-detail.component.html',
  styleUrls: ['./book-detail.component.scss']
})
export class BookDetailComponent implements OnInit {
  @Input() book;
  constructor(private ApiBookService: ApiBookService, private router: Router) { }

  async ngOnInit() {
    this.book = await this.ApiBookService.SearchBookById({book_id: 1})
    console.log(this.book)
    }
    
  goBack() {
    this.router.navigateByUrl('admin/book-management/book-list')
  }  
}
