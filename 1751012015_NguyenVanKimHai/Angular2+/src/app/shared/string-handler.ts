import {ArrayHandler} from './array-handler';

const URL_REGEXP = /^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//\[\]=]*)?/g;

export class StringHandler {
  public static parseUrlInString(str: string): string {
    if (!str) {
      return '';
    }
    str = encodeURI(str);
    const regexp = new RegExp(URL_REGEXP);
    let matcheds = str.match(regexp);
    if (matcheds && matcheds.length) {
      matcheds = ArrayHandler.uniqueArray(matcheds);
      matcheds.forEach(item => {
        str = str.split(item).join(`<a href="${item}">${item}</a>`);
      });
    }
    str = decodeURI(str);
    return str;
  }

  public static createHandle(str: string) {
    if (str) {
      str = str.trim();
      str = str.toLowerCase();
      str = str.replace(/à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ/g, 'a');
      str = str.replace(/è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ/g, 'e');
      str = str.replace(/ì|í|ị|ỉ|ĩ/g, 'i');
      str = str.replace(/ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ/g, 'o');
      str = str.replace(/ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ/g, 'u');
      str = str.replace(/ỳ|ý|ỵ|ỷ|ỹ/g, 'y');
      str = str.replace(/đ/g, 'd');
      str = str.replace(/\,/g, '-');
      str = str.replace(/\_/g, '-');
      str = str.replace(/\./g, '-');
      str = str.replace(/\!/g, '-');
      str = str.replace(/\?/g, '-');
      str = str.replace(/\~/g, '-');
      str = str.replace(/\ /g, '-');
      str = str.replace(/\|/g, '-');
      str = str.replace(/\./g, '-');
      str = str.replace(/\"/g, '-');
      str = str.replace(/\'/g, '-');
      str = str.replace(/\s+/g, '-');
      str = str.replace(/[^\w\-]+/g, '');
      str = str.replace(/\-\-+/g, '-');
      str = str.replace(/^-+/, '');
      str = str.replace(/-+$/, '');
      if (str.slice(-1) == '-') {
        str = str.substring(0, str.length - 1);
      }
    }
    return str;
  }

  public static convertVietnameseString(str: string) {
    if (str) {
      str = str.trim();
      str = str.toLowerCase();
      str = str.replace(/à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ/g, 'a');
      str = str.replace(/è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ/g, 'e');
      str = str.replace(/ì|í|ị|ỉ|ĩ/g, 'i');
      str = str.replace(/ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ/g, 'o');
      str = str.replace(/ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ/g, 'u');
      str = str.replace(/ỳ|ý|ỵ|ỷ|ỹ/g, 'y');
      str = str.replace(/đ/g, 'd');
    }
    return str;
  }

  public static parseHtmlSpecialCharacters(str: string) {
    return str?.trim()
      .replace(/<strong>/g, '$8+')
      .replace(/<\/strong>/g, '$8-')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/<=/g, '&le;')
      .replace(/>=/g, '&ge;')
      .replace(/(\$8\+)/g, '<strong>')
      .replace(/(\$8-)/g, '</strong>');
  }

  public static trimAllSpace(str: string) {
    return str?.replace(/\s+/g, '');
  }

  public static trimAllSpaceOutsideQuotes(str: string) {
    return str?.replace(/\s+(?=([^"]*"[^"]*")*[^"]*$)/g, '');
  }

  public static trimNewLineCharacters(str: string) {
    return str?.replace(/\r?\n|\r/g, '');
  }

  public static trimHtml(html: string) {
    const _tempDIV = document.createElement('div');
    _tempDIV.innerHTML = html;
    return _tempDIV.textContent || _tempDIV.innerText || '';
  }

  public static trimFields(obj, fields: string[]) {
    fields.forEach(f => {
      obj[f] = obj[f] && obj[f].trim();
    });
    return obj;
  }

  public static validatePhoneNumber(phone: string) {
    return !!(this.trimAllSpace(phone) && phone?.match(/^0[0-9]{9,10}$/));
  }

  public static validateEmail(email: string) {
    return !!(this.trimAllSpace(email) && email?.match(
      /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    ));
  }

  public static validateWebsiteUrl(url: string) {
    return !!(this.trimAllSpace(url) && url?.match(/^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$/));
  }

}
