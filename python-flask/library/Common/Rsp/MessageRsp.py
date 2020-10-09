class SendMessageRsp():
    def __init__(self, req):
        self.conversation_id = req['conversation_id'] if req['conversation_id'] else None
        self.content = req['content'] if req['content'] else None
        self.account_id = req['account_id'] if req['account_id'] else None
        self.created_at = req['created_at'] if req['created_at'] else None

    def serialize(self):
        return {"conversation_id": self.conversation_id, "content": self.content, "account_id": self.account_id}
