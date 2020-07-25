import { Component, OnInit } from '@angular/core';
import {FormControl} from '@angular/forms';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  myControl = new FormControl();
  options: string[] = ['One', 'Two', 'Three'];
  ngOnInit() {
    toastr.success("dsadas");
  }
}
