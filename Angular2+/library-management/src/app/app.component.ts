import {Component, OnInit} from '@angular/core';
import { ModalController } from './core/modal-controller/modal-controller.service';
import { TestModalControlerComponent } from './pages/test-modal-controler/test-modal-controler.component';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{

  constructor() {
  }
  ngOnInit() {
  }

}
