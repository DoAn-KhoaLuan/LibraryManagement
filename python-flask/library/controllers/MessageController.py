from flask import request, jsonify

from library import app
from library.BLL import MessageSvc
from library.Common.Req.MessageReq import GetMessagesInConversationByFilterReq, SendMessageReq
from library.Common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from library.Common.Rsp.MessageRsp import SendMessageRsp


@app.route('/message/get-messages', methods=['POST', 'GET'])
def GetMessage():
    req = GetMessagesInConversationByFilterReq(request.json)
    print(req)
    result = MessageSvc.GetMessagesInConversationByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['messages']).serialize()
    return jsonify(res)

@app.route('/message/send-message', methods=['POST', 'GET'])
def SendMessage():
    req = SendMessageReq(request.json)
    result = MessageSvc.SendMessage(req)
    res = SendMessageRsp(result).serialize()
    return jsonify(res)
