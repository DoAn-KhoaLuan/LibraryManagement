import { Router } from '@angular/router';
import { FormBuilder } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-create-book',
  templateUrl: './create-book.component.html',
  styleUrls: ['./create-book.component.scss']
})
export class CreateBookComponent implements OnInit {

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

  constructor(private fb : FormBuilder, private router: Router) { }

  ngOnInit() {
    this.createBookForm.valueChanges.subscribe(data => {
      console.log(data)
    })
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
}
