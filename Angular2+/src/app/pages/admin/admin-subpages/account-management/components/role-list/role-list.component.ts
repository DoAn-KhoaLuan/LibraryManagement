import { Component, OnInit } from '@angular/core';
import {ApiRoleService} from '../../../../../../API/api-role.service';
import {Router} from '@angular/router';
import {ModalController} from '../../../../../../core/modal-controller/modal-controller.service';
import {UpdateUserModalComponent} from '../../../setting-management/user-info/update-user-modal/update-user-modal.component';
import {CreateRoleModalComponent} from './create-role-modal/create-role-modal.component';

@Component({
  selector: 'app-role-list',
  templateUrl: './role-list.component.html',
  styleUrls: ['./role-list.component.scss']
})
export class RoleListComponent implements OnInit {
  roles = [];
  constructor(
    private apiRoleService: ApiRoleService,
    private router: Router,
    private modalController: ModalController,
  ) { }

  async ngOnInit() {
    this.roles = await this.apiRoleService.GetRoles().then();
  }

  onViewRoleDetail(role_id) {
    this.router.navigateByUrl(`/admin/account-management/role-detail/${role_id}`);
  }

  openCreateRoleModal() {
    const modal = this.modalController.create({
      component: CreateRoleModalComponent,
      cssClass: "modal-xl",
      componentProps: {
      },
    });
    modal.show().then();
    modal.onDismiss().then(async role =>  {
      console.log(role)
      if (role) {
        try {
          await this.apiRoleService.CreateRole(role);
          toastr.success("Thêm mới vai trò thành công.")
          this.roles = await this.apiRoleService.GetRoles().then();
        } catch(e) {
          toastr.error("Thêm mới vai trò thất bại.", e.msg || e.message)
        }

      }
    });
  }
}
