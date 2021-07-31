import { MaterialModule } from 'src/app/shared/material.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatInputComponent } from './mat-input.component';
import {MaterialInputAutocompleteComponent} from '../material-input-autocomplete';
import {PipeModule} from '../../pipes/pipe/pipe.module';

@NgModule({
  imports: [
    CommonModule,
    MaterialModule,
    PipeModule
  ],
  declarations: [MatInputComponent, MaterialInputAutocompleteComponent],
  exports: [
    MatInputComponent,
    MaterialInputAutocompleteComponent
  ]
})
export class MatInputModule { }
