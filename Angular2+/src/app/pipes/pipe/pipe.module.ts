import {standardizedId, VND} from './common.pipe';
import {NgModule, Injectable} from '@angular/core';
import {CommonModule} from '@angular/common';
import {SafeHtmlPipe} from './safe-html.pipe';
import {LocationCompactPipe} from './location.pipe';

@Injectable({providedIn: 'root'})
@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [standardizedId, VND, SafeHtmlPipe, LocationCompactPipe],
  exports: [
    standardizedId,
    VND,
    SafeHtmlPipe,
    LocationCompactPipe
  ],
  providers: [LocationCompactPipe]
})
export class PipeModule {
}
