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

  sendMessage(doAnOuGroupId, msg, enableHTML = true) {


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

  testMessage() {
    const msg = `Hello <strong>Trường Đẹp Trai</strong>`;
    console.log('Hello');
    try {
      this.sendMessage(this.groupId, msg);
    } catch (e) {
      debug.log('ERROR in send testMessage: ', e);
    }
  }
}
