from library.Common.Req.MessageReq import GetMessagesInConversationByFilterReq, SendMessageReq
from library.DAL import MessageRep


def GetMessagesInConversationByPage(req:  GetMessagesInConversationByFilterReq):
    has_next, has_prev, messages = MessageRep.GetMessagesInConversationByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "messages": messages
    }
    return result

def SendMessage(req: SendMessageReq):
    result = MessageRep.SendMessage(req)
    return result
