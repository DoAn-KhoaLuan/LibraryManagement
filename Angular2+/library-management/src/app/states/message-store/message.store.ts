import {GetItemsByPageRsp} from "../../models/resp";
import {filter_page} from "../../models/app-models";
import {Injectable} from "@angular/core";
import {EntityStore, StoreConfig} from "@datorama/akita";

export interface MessageState {
  messages_list: any,
  message_list_view: GetItemsByPageRsp;
  filter_page: filter_page,
  active_conversation_id: Number
}

const initState = {
  active_conversation_id:1,
  messages_list : [],
  message_list_view : null,
  filter_page: {
    page: 0,
    per_page: 10,
  },
}
@Injectable({providedIn: 'root'})
@StoreConfig({name:'message'})
export class MessageStore extends EntityStore<MessageState>{
  constructor() {
    super(initState);
  }
}
