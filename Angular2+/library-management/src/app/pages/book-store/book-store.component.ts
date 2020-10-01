import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { WebSocketService } from 'src/app/services/web-socket.service';
import * as io from 'socket.io-client';
import { Message } from 'src/app/models/app-models';
import { AccountQuery } from 'src/app/states/account-store/account.query';
@Component({
  selector: 'app-book-store',
  templateUrl: './book-store.component.html',
  styleUrls: ['./book-store.component.scss']
})
export class BookStoreComponent implements OnInit {
  @ViewChild('mes',{static: false}) message: ElementRef;
  reply_messages = []
  send_messages = []
  messages : any[] =[];
  constructor(private webSocketService: WebSocketService, private accountQuery:AccountQuery) { }
  chatText = ''
  ngOnInit() {
    this.webSocketService.emit('join', {'auth_info': JSON.parse(localStorage.getItem('auth_info')), 'room': "ROOM"});
    this.webSocketService.listen('message').subscribe(data => {
      this.ListenMessage(data)
    })
  }

  ListenMessage(data) {
    let account_id_from_server = data['auth_info'] && data['auth_info']['current_account']['account_id'];
    let account_id_from_client = this.accountQuery.getValue().auth_info.current_account.account_id;
    const isReplyMessage = account_id_from_server != account_id_from_client
    
    if(isReplyMessage) {
      let mess = {
        type:'reply',
        content: data['msg']
      }
      this.messages.push(mess);
    }
    this.MessageScrollToBottom()
  }

  SendMessage() {
    this.webSocketService.emit('incoming-msg', {'msg': this.chatText,
    'auth_info': JSON.parse(localStorage.getItem('auth_info')), 'room': "ROOM"});
    const sendMessage = {
      type: 'send',
      content: JSON.parse(JSON.stringify(this.chatText)) 
    };
    this.messages.push(sendMessage);
    this.chatText='';
    this.MessageScrollToBottom()
  }

  LeaveRoom() {
    this.webSocketService.emit('leave', {'room': 'ROOM'})
  }
  
  MessageScrollToBottom() {
    this.message.nativeElement.scrollTop=this.message.nativeElement.scrollHeight;
  }
}
