import {BaseModel, Processing} from '../core/base-model';

export class Province extends BaseModel {
  code: string;
  name: string;
  filter_name?: string;
}

export class District extends BaseModel {
  code: string;
  province_code?: string;
  name: string;
  filter_name?: string;
}

export class Ward extends BaseModel {
  code: string;
  district_code?: string;
  name: string;
  filter_name?: string;
}

export class CustomRegion extends BaseModel {
  created_at: Date;
  description: string;
  id: string;
  name: string;
  province_codes: string[];
  updated_at: Date;
}
