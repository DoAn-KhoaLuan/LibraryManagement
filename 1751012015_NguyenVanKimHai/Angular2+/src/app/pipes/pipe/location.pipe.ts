import {Injectable, Pipe, PipeTransform} from '@angular/core';

@Pipe({
  name: 'locationCompact'
})
@Injectable()
export class LocationCompactPipe implements PipeTransform {
  transform(value: string, ...args: any[]): any {
    if (!value) {
      return '';
    }
    let result = value.slice(0);
    result = result.replace(/Tỉnh/gim, 'T.');
    result = result.replace(/Huyện/gim, 'H.');
    result = result.replace(/Thành phố/gim, 'TP.');
    // NOTE: Quận 1, Quận 10,... no need to transformed to compact
    result = result.length > 7 ? result.replace(/Quận/gim, 'Q.') : result;
    result = result.replace(/Thị xã/gim, 'Tx.');
    result = result.replace(/Phường/gim, 'P.');
    result = result.replace(/Xã/gim, 'X.');
    result = result.replace(/Thị trấn/gim, 'Tt.');
    result = result.replace(/Hồ Chí Minh/gim, 'HCM');
    return result;
  }
}

@Pipe({
  name: 'addressDisplay'
})
@Injectable()
export class AddressDisplayPipe implements PipeTransform {

  constructor(
    private locationCompact: LocationCompactPipe
  ) {
  }

  transform(value, debug = false, ...args): any {
    if (!value || !value.province) {
      return '';
    }
    let {address1, ward, district, province} = value;
    ward = ward && this.locationCompact.transform(ward);
    district = district && this.locationCompact.transform(district);
    province = province && this.locationCompact.transform(province);
    return `${address1}${ward && ', ' + ward}, ${district}, ${province}`;
  }
}
