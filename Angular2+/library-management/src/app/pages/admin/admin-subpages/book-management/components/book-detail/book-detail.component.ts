import { ConfirmDeleteModalComponent } from './confirm-delete-modal/confirm-delete-modal.component';
import { ModalController } from './../../../../../../core/modal-controller/modal-controller.service';
import { Router } from '@angular/router';
import { ApiBookService } from './../../../../../../API/api-book.service';
import { Component, OnInit, Input, OnChanges, ChangeDetectorRef } from '@angular/core';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-book-detail',
  templateUrl: './book-detail.component.html',
  styleUrls: ['./book-detail.component.scss']
})
export class BookDetailComponent implements OnInit, OnChanges {
  @Input() book;
  isEditing = false;
  constructor(private ApiBookService: ApiBookService, private router: Router, private fb: FormBuilder, private ref: ChangeDetectorRef, private modalController: ModalController) { }
  updateBookForm = this.fb.group({
    book_name: [''],
    author_name: [''],
    contact_name: [''],
    category_name: [''],
    page_number: [''],
    cost_price: [''],
    retail_price: [''],
    discount: [''],
    description: [''],
    notes: [''],
  });
  async ngOnInit() {
    this.book = await this.ApiBookService.SearchBookById({book_id: 1});
    this.updateBookForm.valueChanges.subscribe(data => {
    })
  }

  ngOnChanges() {
    this.setupDataForm()
  }
  onClickUpdateBtn() {
    if(this.isEditing) {
    } else {
      // chuyển qua view update
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
        
      },
    });
    modal.show().then();
    modal.onDismiss().then();
  }

  setupDataForm() {
    this.updateBookForm.patchValue({
      'book_name': this.book?.book_name,
      'author_name': this.book?.author.author_name,
      'contact_name': this.book?.supplier.contact_name,
      'category_name': this.book?.category.category_name,
      'page_number': this.book?.page_number,
      'cost_price': this.book?.cost_price,
      'retail_price': this.book?.retail_price,
      'discount': this.book?.discount,
      'description': this.book?.description,
    });
    this.ref.detectChanges();
  }

  
}
