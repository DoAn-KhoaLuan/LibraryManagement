import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class TelegramApi {

  constructor(
    private http: HttpClient,
  ) {}

  sendMessage(doAnOuGroupId, msg, enableHTML = true) {
    const doAnOuUrl =
      'https://api.telegram.org/bot1704225056:AAFXTHV_JiyGYkHBBlI24ByE_oRcH_SSaqg/sendMessage';
    const doAnOuData: any = {
      chat_id: doAnOuGroupId,
      text: msg
    };
    if (enableHTML) {
      doAnOuData.parse_mode = 'HTML';
    }

    return this.http.post(doAnOuUrl, doAnOuData).toPromise();
  }

}
