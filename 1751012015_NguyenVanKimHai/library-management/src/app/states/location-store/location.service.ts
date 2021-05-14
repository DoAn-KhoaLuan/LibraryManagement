import {Injectable} from '@angular/core';
import {District, Province, Ward} from '../../models/Location';
import {LocationStore} from './location.store';
import {LocationQuery} from './location.query';
import {StringHandler} from '../../shared/string-handler';
import {LocationCompactPipe} from '../../pipes/pipe/location.pipe';
import {ApiLocation} from '../../API/api-location';

@Injectable({
  providedIn: 'root'
})
export class LocationService {

  constructor(
    private locationCompact: LocationCompactPipe,
    private locationApi: ApiLocation,
    private locationStore: LocationStore,
    private locationQuery: LocationQuery
  ) {
  }

  private static sortProvinces(provinces) {
    provinces.forEach(p => p.name = p.name.replace(/Tỉnh |Thành phố /g, ''));
    provinces.sort((a, b) => StringHandler.convertVietnameseString(a.name) > StringHandler.convertVietnameseString(b.name) ? 1 : -1);
    const priorities = ['79', '01', '48', '92'];
    const priProvinces = provinces.filter(p => {
      switch (p.code) {
        case '79':
          p.priority = 1;
          return true;
        case '01':
          p.priority = 2;
          return true;
        case '48':
          p.priority = 3;
          return true;
        case '92':
          p.priority = 4;
          return true;
        default:
          return false;
      }
    });
    provinces = provinces.filter(p => priorities.indexOf(p.code) < 0);
    priProvinces.sort((a, b) => a.priority > b.priority ? 1 : -1);

    provinces = priProvinces.concat(provinces);

    return provinces;
  }

  private static sortByName(data) {
    return data.sort((a, b) => StringHandler.convertVietnameseString(a.name) > StringHandler.convertVietnameseString(b.name) ? 1 : -1);
  }

  async initLocations() {
    try {
      const {provincesList, districtsList, wardsList} = this.locationQuery.getValue();
      if (!provincesList?.length) {
        await this.listProvinces();
      }
      if (!districtsList?.length) {
        await this.listDistricts();
      }
      if (!wardsList?.length) {
        await this.listWards();
      }
      this.setLocationReady(true);
    } catch (e) {
      debug.error('ERROR in init location service', e);

      setTimeout(_ => {
        this.initLocations();
      }, 1000);
    }
  }

  private setLocationReady(ready: boolean) {
    this.locationStore.update({locationReady: ready});
  }

  async listProvinces() {
    try {
      const res = await this.locationApi.listProvinces();
      res.provinces = LocationService.sortProvinces(res.provinces);
      const provinces = res.provinces.map(p => new Province({
        ...p,
        id: p.code,
        filter_name: p.name
      }));
      this.locationStore.update({provincesList: provinces});
    } catch (e) {
      debug.log('ERROR in listProvinces', e);
      throw e;
    }
  }

  private async listDistricts() {
    try {
      const res = await this.locationApi.listDistricts();
      res.districts = LocationService.sortByName(res.districts);
      const districts: District[] = res.districts.map(d => {
        const _province = this.locationQuery.getProvince(d.province_code);
        const province_name = _province && this.locationCompact.transform(_province.name);

        return new District({
          ...d,
          id: d.code,
          filter_name: `${province_name} - ${this.locationCompact.transform(d.name)}`
        });
      });
      this.locationStore.update({districtsList: districts});
    } catch (e) {
      debug.log('ERROR in listDistricts', e);
      throw e;
    }
  }

  private async listWards() {
    try {
      const res = await this.locationApi.listWards();
      res.wards = LocationService.sortByName(res.wards);
      const wards: Ward[] = res.wards.map(w => {

        const _district: District = this.locationQuery.getDistrict(w.district_code);
        const _province = this.locationQuery.getProvince(_district?.province_code);
        const province_name = _province && this.locationCompact.transform(_province.name);
        const district_name = _district && this.locationCompact.transform(_district.name);

        return new Ward({
          ...w,
          id: w.code,
          filter_name: `${province_name} - ${district_name} - ${this.locationCompact.transform(w.name)}`
        });
      });
      this.locationStore.update({wardsList: wards});
    } catch (e) {
      debug.log('ERROR in listWards', e);
      throw e;
    }
  }

  /**
   * @deprecated make an Observable for each Component instead, using combineLatest of
   * locationQuery.select("districtsList") + formControl["provinceCode"].valueChanges
   */
  filterDistrictsByProvince(provinceCode: string) {
    const _districts = this.locationQuery.getValue().districtsList;
    return _districts?.filter(dist => dist.province_code == provinceCode);
  }

  /**
   * @deprecated make an Observable for each Component instead, using combineLatest of
   * locationQuery.select("wardsList") + formControl["districtCode"].valueChanges
   */
  filterWardsByDistrict(districtCode: string) {
    const _wards = this.locationQuery.getValue().wardsList;
    return _wards?.filter(dist => dist.district_code == districtCode);
  }

}
