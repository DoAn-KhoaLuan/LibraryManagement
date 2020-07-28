/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { TestModalControlerComponent } from './test-modal-controler.component';

describe('TestModalControlerComponent', () => {
  let component: TestModalControlerComponent;
  let fixture: ComponentFixture<TestModalControlerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TestModalControlerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TestModalControlerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
