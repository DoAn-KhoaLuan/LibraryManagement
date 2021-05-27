export abstract class BaseModel {
  id: string;
  public constructor(obj) {
    this['o_data'] = obj;
    for (const key in obj) {
      if (obj.hasOwnProperty(key)) {
        this[key] = obj[key];
      }
    }
  }
}

export interface Processing {
  p_data: any;
}
