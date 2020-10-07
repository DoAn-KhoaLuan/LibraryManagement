import { account } from './../../models/app-models';
import {Injectable} from "@angular/core";
import {ApiMessageService} from "../../API/api-message.service";
import {MessageStore} from "./message.store";
import {MessageQuery} from "./message.query";
import {GetItemsByPageRsp} from "../../models/resp";
import {AccountQuery} from "../account-store/account.query";
import {AccountStore} from "../account-store/account.store";
import {AccountService} from "../account-store/account.service";

@Injectable({
  providedIn: 'root'
})
export class MessageService {
  constructor(private apiMessageService:ApiMessageService,
              private messageStore: MessageStore,
              private messageQuery: MessageQuery,
              private accountQuery: AccountQuery,
              private accountStore: AccountStore,
              private accountService: AccountService
  ) {
  }

  async GetMoreMessageAndPushIntoStore(filter) {
    let res: GetItemsByPageRsp = await this.apiMessageService.GetMessages(filter);
    let new_messages = res.items;
    let account_id_from_client = this.accountQuery.getValue().auth_info.current_account.account_id;

    new_messages.forEach( mess => {
      if(mess.account_id == account_id_from_client) {
        mess.type = 'send'
      } else {
        mess.type = 'reply'
      }
    })

    let messages_list = [...this.messageQuery.getValue().messages_list];
    messages_list.push(...new_messages)
    this.messageStore.update({messages_list: messages_list})
  }

  async SendMessage(content) {
    const sendMessageReq = {
      conversation_id : this.messageQuery.getValue().active_conversation_id,
      account_id : this.accountQuery.getValue().auth_info.current_account.account_id,
      content : content,
    }
    return await this.apiMessageService.SendMessage(sendMessageReq);
  }

  SetActiveConversationId(conversation_id) {
    this.messageStore.update({active_conversation_id: conversation_id})
  }
}
