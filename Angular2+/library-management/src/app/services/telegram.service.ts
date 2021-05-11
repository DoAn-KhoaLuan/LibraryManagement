import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {StringHandler} from '../shared/string-handler';

@Injectable({
  providedIn: 'root'
})
export class TelegramService {
  groupId = '-436944285';

  constructor(
    private http: HttpClient,
  ) {
  }

  async sendMessage(doAnOuGroupId, msg, enableHTML = true) {
    const doAnOuUrl =
      'https://api.telegram.org/bot1704225056:AAFXTHV_JiyGYkHBBlI24ByE_oRcH_SSaqg/sendMessage';
    const doAnOuData: any = {
      chat_id: doAnOuGroupId,
      text: StringHandler.parseHtmlSpecialCharacters(msg)
    };
    if (enableHTML) {
      doAnOuData.parse_mode = 'HTML';
    }

    return this.http.post(doAnOuUrl, doAnOuData).toPromise();
  }

  async sendCreateCustomerAccount(account, customer) {
    const msg = `
<strong>ĐĂNG KÝ TÀI KHOẢN KHÁCH HÀNG!</strong>
-----------------------------
Họ tên: <strong>${customer.last_name} ${customer.first_name}</strong>
Số điện thoại: <strong>${customer.phone}</strong>
Email: ${customer.email}
Tên tài khoản: ${account.account_name}
    `;
    try {
      await this.sendMessage(this.groupId, msg);
    } catch (e) {
      debug.log('ERROR in send testMessage: ', e);
    }
  }

  async sendCreateOrder(order) {
    let order_line_string = '';
    for (let line of order.order_details) {
      order_line_string += `
- ${line.quantity} x ${
        line.book.book_name
      } - ${this.moneyFormat(line.retail_price)}`;
    }
    // let fee_line_string = '';
    // for (let line of order.fee_lines) {
    //   fee_line_string += `- <i>${line.name}: ${this.moneyFormat(
    //     line.amount
    //   )}</i>\n`;
    // }
    const msg = `
<strong>TẠO ĐƠN HÀNG THÀNH CÔNG!</strong>
-----------------------------
Khách hàng: ${order?.customer?.last_name || ""} ${order?.customer?.first_name || ""}
Nhân viên: ${order?.employee?.last_name || ""} ${order?.employee?.first_name || ""} 
Sản phẩm: ${order_line_string}
Tổng tiền: ${this.moneyFormat(order?.total)}
Hình thức: ${order?.type == "online" ? "Mua hàng online" : "Mua tại chỗ"}
    `;
    try {
      console.log(order)
      await this.sendMessage(this.groupId, msg);
    } catch (e) {
      debug.log('ERROR in send testMessage: ', e);
    }
  }

  moneyFormat(value: any): string {
    if (typeof value != "number" && typeof value != "string") {
      return value;
    }
    if (typeof value == "string") {
      value = Number(value);
    }
    const valueString = value < 0 ?  (-value).toString() : value.toString();

    if (valueString.includes(".")) {
      const wholePart = valueString.split(".")[0]
        .replace(/./g, (match, p1, p2) => {
          return p1 && match !== "," && ((p2.length - p1) % 3 === 0) ? '.' + match : match;
        });
      const decimalPart = valueString.split(".")[1];

      return `${value < 0 ? '-' : ''}${wholePart},${decimalPart}`;
    } else {
      const result = valueString.replace(/./g, (match, p1, p2) => {
        return p1 && match !== "," && ((p2.length - p1) % 3 === 0) ? '.' + match : match;
      });
      return `${value < 0 ? '-' : ''}${result} ₫`;
    }
  }
}
