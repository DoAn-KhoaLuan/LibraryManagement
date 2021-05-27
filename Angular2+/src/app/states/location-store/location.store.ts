import {Injectable} from '@angular/core';
import {District, Province, Ward} from '../../models/Location';
import {Store, StoreConfig} from '@datorama/akita';

export interface StateLocation {
  provincesList: Province[];
  districtsList: District[];
  wardsList: Ward[];

  locationReady: boolean;
}

const initialState = {
  provincesList: [],
  districtsList: [],
  wardsList: [],

  locationReady: false
};

@Injectable({
  providedIn: 'root'
})
@StoreConfig({name: 'location'})
export class LocationStore extends Store<StateLocation> {
  constructor() {
    super(initialState);
  }
}
