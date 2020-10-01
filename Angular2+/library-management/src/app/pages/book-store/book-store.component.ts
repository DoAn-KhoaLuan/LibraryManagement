import { Component, OnInit } from '@angular/core';
import { WebSocketService } from 'src/app/services/web-socket.service';
import * as io from 'socket.io-client';
@Component({
  selector: 'app-book-store',
  templateUrl: './book-store.component.html',
  styleUrls: ['./book-store.component.scss']
})
export class BookStoreComponent implements OnInit {

  constructor(private webSocketService: WebSocketService) { }
  chatText = ''
  ngOnInit() {
    this.webSocketService.socket.on('event', function(data) {
      console.log("asdsadsa")
    })
  }

  SendMessage() {
    this.webSocketService.emit('event',this.chatText)
  }
}
