export class ArrayHandler {
  public static uniqueArray(arr: any[]): any[] {
    let hash = {};
    let result = [];
    arr.forEach(item => {
      if (!hash[item]) {
        hash[item] = 1;
      }
    });
    for (let i in hash) {
      if (hash.hasOwnProperty(i) && hash[i] === 1) {
        result.push(i);
      }
    }
    return result;
  }

  public static upsert(arr: any[], item) {
    const i = arr.findIndex(_item => _item.id == item.id);
    if (i > -1) {
      arr[i] = item;
    } else {
      arr.push(item);
    }
    return arr;
  }
}
