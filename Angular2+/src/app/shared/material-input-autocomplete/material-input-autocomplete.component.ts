import {
  ChangeDetectorRef,
  Component,
  EventEmitter,
  Input,
  OnChanges,
  OnInit,
  Output,
  SimpleChanges,
  ViewChild
} from '@angular/core';
import {NG_VALUE_ACCESSOR} from '@angular/forms';
import {MatAutocompleteSelectedEvent} from '@angular/material/autocomplete';
import {ValueAccessorBase} from '../ValueAccessorBase';
import {StringHandler} from '../string-handler';
import {MaterialInput} from '../material-input.interface';
import {MatInput} from '@angular/material/input';

@Component({
  selector: 'app-material-input-autocomplete',
  templateUrl: './material-input-autocomplete.component.html',
  styleUrls: ['./material-input-autocomplete.component.scss'],
  providers: [
    {provide: NG_VALUE_ACCESSOR, useExisting: MaterialInputAutocompleteComponent, multi: true}
  ]
})
export class MaterialInputAutocompleteComponent extends ValueAccessorBase<any> implements OnInit, OnChanges, MaterialInput {
  @ViewChild('input', { static: true }) input: MatInput;

  @Input() appearance: any;
  @Input() textLabel: string;
  @Input() placeholder: string;
  @Input() options: any[] = [];
  @Input() displayMap: (any) => string;
  @Input() valueMap: (any) => string;
  @Input() error = false;
  @Input() register = false;
  @Input() errorMessage: string;
  @Input() disabled: boolean;

  @Output() optionSelect = new EventEmitter();

  filteredOptions: any[] = [];
  remainedOptions: any[] = [];

  searchValue: string;

  constructor(
    private cdr: ChangeDetectorRef
  ) {
    super();
  }

  ngOnInit() {
    this.remainedOptions = this.options;
  }

  ngOnChanges(changes: SimpleChanges) {
    const options = changes.options;
    if (options && options.currentValue) {
      this.remainedOptions = options.currentValue;
      this.writeValue(this.value);
    }
  }

  onSearch() {
    this.filteredOptions = this.searchValue ? this._filter(this.searchValue) : JSON.parse(JSON.stringify(this.remainedOptions));
    if (!this.searchValue) {
      this.value = null;
    }
    this.cdr.detectChanges();
  }

  onSelectOption(event: MatAutocompleteSelectedEvent) {
    this.value = this.valueMap ? this.valueMap(event.option.value) : event.option.value;
    this.input.value = this.displayMap ? this.displayMap(event.option.value) : event.option.value;
  }

  private _filter(value: any): string[] {
    let filterValue = value;
    const displayMap = this.displayMap;
    if (!value) {
      return this.remainedOptions;
    }
    if (typeof value == 'string') {
      filterValue = StringHandler.convertVietnameseString(filterValue);
    }
    if (typeof value == 'object' && displayMap) {
      filterValue = displayMap(filterValue).toLowerCase();
    }
    return this.remainedOptions.filter(
      option => StringHandler.convertVietnameseString((displayMap ? displayMap(option) : option)).indexOf(filterValue) != -1
    );
  }

  writeValue(value: any) {
    super.writeValue(value);
    this.remainedOptions = this.options;

    const option = this.options?.find(opt => (this.valueMap ? this.valueMap(opt) : opt) == value);

    if (option) {
      this.input.value = this.displayMap ? this.displayMap(option) : option;
      this.searchValue = this.displayMap ? this.displayMap(option) : option;
    } else {
      this.input.value = null;
      this.searchValue = null;
    }

  }

  focus() {
    this.input.focus();
  }

}
