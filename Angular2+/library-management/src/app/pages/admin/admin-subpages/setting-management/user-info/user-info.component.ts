import { UpdateUserModalComponent } from './update-user-modal/update-user-modal.component';
import { auth_info } from './../../../../../models/app-models';
import { FormBuilder } from '@angular/forms';
import { ChangePasswordModalComponent } from './../../account-management/components/account-detail/change-password-modal/change-password-modal.component';
import { AccountQuery } from './../../../../../states/account-store/account.query';
import { ModalController } from './../../../../../core/modal-controller/modal-controller.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-user-info',
  templateUrl: './user-info.component.html',
  styleUrls: ['./user-info.component.scss']
})
export class UserInfoComponent implements OnInit {
  auth_info$ = this.accountQuery.auth_info$
  user_info
  constructor(
    private accountQuery: AccountQuery,
    private modalController: ModalController,
    private fb: FormBuilder
  ) { }

  ngOnInit() {
    this.accountQuery.auth_info$.subscribe(auth_info => {
      this.user_info = auth_info.user_info
      console.log(this.user_info)
    })
  }

  OpenChangePasswordModal() {
    const modal = this.modalController.create({
      component: ChangePasswordModalComponent,
      cssClass: "modal-lg",
      componentProps: {
        account_id: this.user_info.account.account_id
      },
    });
    modal.show().then();
  }

  OpenUpdateUserModal() {
    const modal = this.modalController.create({
      component: UpdateUserModalComponent,
      cssClass: "modal-xl",
      componentProps: {
        account_id: this.user_info.account.account_id
      },
    });
    modal.show().then();
  }
}
