import { BookQuery } from './../../../../../../states/book-store/book.query';
import { ConfirmDeleteModalComponent } from './confirm-delete-modal/confirm-delete-modal.component';
import { ModalController } from './../../../../../../core/modal-controller/modal-controller.service';
import { Router, ActivatedRoute } from '@angular/router';
import { ApiBookService } from './../../../../../../API/api-book.service';
import { Component, OnInit, Input, OnChanges, ChangeDetectorRef } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { BookService } from 'src/app/states/book-store/book.service';

@Component({
  selector: 'app-book-detail',
  templateUrl: './book-detail.component.html',
  styleUrls: ['./book-detail.component.scss']
})
export class BookDetailComponent implements OnInit, OnChanges {
  isEditing = false;
  detail_book$ = this.bookQuery.detail_book$;
  constructor(
    private bookQuery: BookQuery,
    private bookService: BookService,
    private router: Router,
    private fb: FormBuilder,
    private ref: ChangeDetectorRef,
    private route: ActivatedRoute,
    private modalController: ModalController) { }

    updateBookForm = this.fb.group({
      book_id: [''],
      book_name: [''],
      author_name: [''],
      supplier_name: [''],
      category_name: [''],
      page_number: [''],
      cost_price: [''],
      retail_price: [''],
      discount: [''],
      description: [''],
      note: [''],
    });
  async ngOnInit() {
    const req = {
      book_id: parseInt(this.route.snapshot.params['id'])
    }
    const res = await this.bookService.searchBooks(req);
    const detail_book = res.books[0];
    this.bookService.setDetailBook(detail_book);
  }

  ngOnChanges() {
    this.setupDataForm()
  }

  async onClickUpdateBtn() {
    if(this.isEditing) {
      let update_book = this.updateBookForm.value;
      await this.bookService.UpdateBook(update_book)
    } else {
      this.toggleEdit();
      this.setupDataForm();
    }
  }
    
  goBack() {
    if(this.isEditing) {
      this.toggleEdit()
    } else {
      this.router.navigateByUrl('admin/book-management/book-list')
    }
  }  

  toggleEdit() {
    this.isEditing = !this.isEditing;
  }

  onOpenDeleteModal() {
    const modal = this.modalController.create({
      component: ConfirmDeleteModalComponent,
      componentProps: {
        book: this.bookQuery.getValue().detail_book
      },
    });
    modal.show().then();
    modal.onDismiss().then(delete_book => {
      if(delete_book) {
        try {
          this.bookService.DeleteBookById(delete_book.book_id)
          this.router.navigateByUrl('admin/book-management/book-list')
          toastr.success("Bạn đã xóa sách thành công")
        } catch(e) {
          toastr.error("Xóa sách không thành thông", e.msg || e.message)
        }
      }
    });
  }

  setupDataForm() {
    let store_detail_book = this.bookQuery.getValue().detail_book; 
    this.updateBookForm.patchValue({
      'book_id': store_detail_book?.book_id,
      'book_name': store_detail_book?.book_name,
      'author_name': store_detail_book?.author.author_name,
      'supplier_name': store_detail_book?.supplier.contact_name,
      'category_name': store_detail_book?.category.category_name,
      'page_number':store_detail_book?.page_number,
      'cost_price': store_detail_book?.cost_price,
      'retail_price':store_detail_book?.retail_price,
      'discount': store_detail_book?.discount,
      'description': store_detail_book?.description,
      'note': store_detail_book?.note
    });
  }

  
}
