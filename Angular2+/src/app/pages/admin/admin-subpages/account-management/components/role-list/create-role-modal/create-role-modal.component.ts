import { Component, OnInit } from '@angular/core';
import {ModalAction} from '../../../../../../../core/modal-controller/modal-action.service';
import {ApiRoleService} from '../../../../../../../API/api-role.service';

@Component({
  selector: 'app-create-role-modal',
  templateUrl: './create-role-modal.component.html',
  styleUrls: ['./create-role-modal.component.scss']
})
export class CreateRoleModalComponent implements OnInit {
  role = {
    role_name: "",
    note: "",
  };
  constructor(
    private modalAction: ModalAction,
    private apiRoleService: ApiRoleService,
  ) { }

  ngOnInit(): void {
  }

  dismissModal() {
    this.modalAction.dismiss(null);
  }

  CreateRole() {
    this.modalAction.dismiss(this.role);
  }
}
