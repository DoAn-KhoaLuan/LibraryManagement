import { ApiCategoryService } from './../../../../../../API/api-book-category.service';
import { BookService } from 'src/app/states/book-store/book.service';
import { Router } from '@angular/router';
import { FormBuilder } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-create-book',
  templateUrl: './create-book.component.html',
  styleUrls: ['./create-book.component.scss']
})
export class CreateBookComponent implements OnInit {
  filter = {
    page : 1,
    per_page : 1000
  }

  createBookForm = this.fb.group({
    book_name: [''],
    author_name: [''],
    contact_name: [''],
    category_name: [''],
    page_number: [''],
    cost_price: [''],
    retail_price: [''],
    discount: [''],
    description: [''],
    note: [''],
  });

  constructor(private fb : FormBuilder, private router: Router, private bookService: BookService) { }

  async ngOnInit() {
    await this.GetAuthors(this.filter)
    await this.GetCategories(this.filter)
    await this.GetSuppliers(this.filter)
  }
  async onCreateUser() {
    // const newReader = {...this.reader};
    // const res = await this.readerService.createReader(newReader);
    // if(res.success) {
    //   toastr.success("Bạn đã tạo mới đọc giả thành công!", "Đăng ký thành công");
    //   this.router.navigateByUrl('/admin/user-management/user-list');
    // } else {
    //   toastr.error("Vui lòng thực hiện lại thao tác!", "Đăng ký thất bại");
    // }
  }

  resetDataForm() {
    this.createBookForm.patchValue({
      'book_name': '',
      'author_name': '',
      'contact_name': '',
      'category_name': '',
      'page_number': '',
      'cost_price': '',
      'retail_price': '',
      'discount': '',
      'description': '',
      'note': '',
    });
  }

  onCreateBook() {
  }

  goBack() {
    this.router.navigateByUrl('admin/book-management/book-list')
  }  

  async GetCategories(filter) {
    await this.bookService.GetCategories(filter)
  }

  async GetSuppliers(filter) {
    await this.bookService.GetSuppliers(filter)
  }

  async GetAuthors(filter) {
    await this.bookService.GetAuthors(filter)
  }
}
