import {Component, OnInit} from '@angular/core';
import { ModalController } from './core/modal-controller/modal-controller.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  loadingPage = false;
  constructor() {
  }
  ngOnInit() {
  }

}
