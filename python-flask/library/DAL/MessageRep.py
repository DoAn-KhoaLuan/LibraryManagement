from datetime import datetime

from library import db
from library.Common.Req.MessageReq import GetMessagesInConversationByFilterReq, SendMessageReq
from library.Common.util import ConvertModelListToDictList
from library.DAL import models


def GetMessagesInConversationByPage(req:  GetMessagesInConversationByFilterReq):
    if req.page == 0:
        total_messages_amount = models.Messages.query.filter(models.Messages.conversation_id == req.conversation_id).count()
        last_page_number = total_messages_amount // req.per_page + 1
        messages_pagination = models.Messages.query.filter(models.Messages.conversation_id == req.conversation_id) \
            .paginate(page=last_page_number, per_page=req.per_page)
        has_next = messages_pagination.has_next
        has_prev = messages_pagination.has_prev
        messages = ConvertModelListToDictList(messages_pagination.items)
        return has_next, has_prev, messages
    else:
        messages_pagination = models.Messages.query.filter(models.Messages.conversation_id == req.conversation_id) \
            .paginate(page=req.page, per_page=req.per_page)
        has_next = messages_pagination.has_next
        has_prev = messages_pagination.has_prev
        messages = ConvertModelListToDictList(messages_pagination.items)
        return has_next, has_prev, messages

def SendMessage(req: SendMessageReq):
    create_message = models.Messages(conversation_id=req.conversation_id, content=req.content, account_id=req.account_id, created_at= datetime.utcnow())
    db.session.add(create_message)
    db.session.commit()
    return create_message.serialize()
