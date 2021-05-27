import {Component, OnInit} from '@angular/core';
import { ApiBookService } from 'src/app/API/api-book.service';
import { ModalAction } from 'src/app/core/modal-controller/modal-action.service';
import { StringHandler } from 'src/app/shared/string-handler';
import { BookQuery } from 'src/app/states/book-store/book.query';

@Component({
    selector: 'app-compare-book-modal',
    templateUrl: './compare-book-modal.component.html',
    styleUrls: ['./compare-book-modal.component.scss'],
  })
export class CompareBookModalComponent implements OnInit {
    book_detail$ = this.bookQuery.detail_book$;
    compare_books; 
    stars: number[] = [1, 2, 3, 4, 5];

    constructor(
        private bookQuery: BookQuery,
        private modalAction: ModalAction,
        private apiBookService: ApiBookService
    ) {}

    async ngOnInit() {
      console.log(this.bookQuery.getValue().detail_book)
      const req = {
        book_name: StringHandler.createHandle(this.bookQuery.getValue().detail_book.book_name)
      };
      this.compare_books = await this.apiBookService.compareBook(req);
    }

    dismissModal() {
      this.modalAction.dismiss(null);
    }
  }