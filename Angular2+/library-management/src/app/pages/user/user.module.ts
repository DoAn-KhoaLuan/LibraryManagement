import { UserRoutingModule } from './user-routing.service';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserComponent } from './user.component';
import { PipeModule } from 'src/app/pipes/pipe/pipe.module';

@NgModule({
  imports: [
    CommonModule,
    UserRoutingModule,
    PipeModule
  ],
  declarations: [UserComponent]
})
export class UserModule { }
