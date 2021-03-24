import {Injectable} from '@angular/core';
import {Query} from '@datorama/akita';
import {LocationStore, StateLocation} from './location.store';

@Injectable({
  providedIn: 'root'
})
export class LocationQuery extends Query<StateLocation> {

  constructor(protected store: LocationStore) {
    super(store);
  }

  getProvince(code: string) {
    const provinces = this.getValue().provincesList;
    return provinces?.find(prov => prov.code == code);
  }

  getDistrict(code: string) {
    const districts = this.getValue().districtsList;
    return districts?.find(dist => dist.code == code);
  }

  getWard(code: string) {
    const wards = this.getValue().wardsList;
    return wards?.find(ward => ward.code == code);
  }

}
