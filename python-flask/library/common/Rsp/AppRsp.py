class DeleteItemRsp():
    def __init__(self, req):
        self.id = req.id

    def serialize(self):
        return {"id": self.id}