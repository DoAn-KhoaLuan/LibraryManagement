# from flask import request, jsonify, session
# from flask_socketio import send, join_room, leave_room
#
# from library import app, socketio
# from library.service import MessageSvc
# from library.common.Req.MessageReq import GetMessagesInConversationByFilterReq, SendMessageReq, \
#     GetConversationByCustomerAccountIdReq, ReadConversationReq
# from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
# from library.common.Rsp.MessageRsp import SendMessageRsp
#
#
# @app.route('/message/get-messages', methods=['POST', 'GET'])
# def GetMessages(): #page = 0, là lấy page cuối cùng, những tin nhắn mới nhất
#     print("request na", request.json)
#     req = GetMessagesInConversationByFilterReq(request.json)
#     result = MessageSvc.GetMessagesInConversationByPage(req)
#     res = GetItemsByPageRsp(hasNext=result['hasNext'], hasPrev=result['hasPrev'],
#                             items=result['messages'], currentPage =result['current_page'] ).serialize()
#     return jsonify(res)
#
# @app.route('/message/get-conversation-by-customer-account-id', methods=['POST', 'GET'])
# def GetConversationByCustomerAccountId():
#     req = GetConversationByCustomerAccountIdReq(request.json)
#     conversation = MessageSvc.GetConversationByCustomerAccountId(req)
#     return jsonify(conversation)
#
# @app.route('/message/get-all-conversations', methods=['POST', 'GET'])
# def GetAllConversations():
#     all_model_conversations = MessageSvc.GetAllConversations()
#     return jsonify(all_model_conversations)
#
#
# @app.route('/message/read-conversation', methods=['POST', 'GET'])
# def ReadConversation():
#     req = ReadConversationReq(request.json)
#     _ = MessageSvc.ReadConversation(req)
#     return jsonify({"is_success": True})
#
# @socketio.on('incoming-msg')
# def on_message(data):
#     """Broadcast messages"""
#     req = SendMessageReq(data)
#     result = MessageSvc.SendMessage(req)
#     res = SendMessageRsp(result).serialize()
#     room = data["room"]
#     print("on message naf")
#     send(res, room=room)
#
#
# @socketio.on('join')
# def on_join(data):
#     """User joins a room"""
#     print('data', data)
#     session['auth_info']=data['auth_info']
#     room = data["room"]
#     print('data: ', data)
#
#     join_room(room)
#     print('join na')
#     # send({"msg":"Someone has join the room"}, room=room)
#
#
# @socketio.on('leave')
# def on_leave(data):
#     """User leaves a room"""
#     room = data['room']
#     leave_room(room)
#     send({"msg":"Someone has left the room"}, room=room)
#
#
