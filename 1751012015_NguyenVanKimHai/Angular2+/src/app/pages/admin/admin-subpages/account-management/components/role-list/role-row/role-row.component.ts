import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-role-row',
  templateUrl: './role-row.component.html',
  styleUrls: ['./role-row.component.scss']
})
export class RoleRowComponent implements OnInit {
  @Input() role_item;
  @Input() index;
  constructor() { }

  ngOnInit(): void {
  }

}
