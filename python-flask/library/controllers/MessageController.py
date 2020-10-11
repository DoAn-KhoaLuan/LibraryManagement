from flask import request, jsonify, session
from flask_socketio import send, join_room, leave_room

from library import app, socketio
from library.BLL import MessageSvc
from library.Common.Req.MessageReq import GetMessagesInConversationByFilterReq, SendMessageReq, \
    GetConversationByCustomerAccountIdReq, ReadConversationReq
from library.Common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from library.Common.Rsp.MessageRsp import SendMessageRsp


@app.route('/message/get-messages', methods=['POST', 'GET'])
def GetMessages(): #page = 0, là lấy page cuối cùng, những tin nhắn mới nhất
    req = GetMessagesInConversationByFilterReq(request.json)
    result = MessageSvc.GetMessagesInConversationByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['messages'], currentPage =result['current_page'] ).serialize()
    return jsonify(res)

@app.route('/message/get-conversation-by-customer-account-id', methods=['POST', 'GET'])
def GetConversationByCustomerAccountId():
    req = GetConversationByCustomerAccountIdReq(request.json)
    conversation = MessageSvc.GetConversationByCustomerAccountId(req)
    return jsonify(conversation)

@app.route('/message/get-all-conversations', methods=['POST', 'GET'])
def GetAllConversations():
    all_model_conversations = MessageSvc.GetAllConversations()
    return jsonify(all_model_conversations)


@app.route('/message/read-conversation', methods=['POST', 'GET'])
def ReadConversation():
    req = ReadConversationReq(request.json)
    _ = MessageSvc.ReadConversation(req)
    return jsonify({"is_success": True})

@socketio.on('incoming-msg')
def on_message(data):
    """Broadcast messages"""
    req = SendMessageReq(data)
    result = MessageSvc.SendMessage(req)
    res = SendMessageRsp(result).serialize()
    room = data["room"]
    send(res, room=room)


@socketio.on('join')
def on_join(data):
    """User joins a room"""
    session['auth_info']=data['auth_info']
    room = data["room"]
    join_room(room)

    send({"content" : "Someone has joined the room."}, room=room)


@socketio.on('leave')
def on_leave(data):
    """User leaves a room"""
    room = data['room']
    leave_room(room)
    send({"msg":"Someone has left the room"}, room=room)


