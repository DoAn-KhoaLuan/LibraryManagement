class DeleteItemReq():
    def __init__(self, req):
        self.id = req['id'] if 'id' in req else None

    def serialize(self):
        return {
            "id": self.id
        }


class SearchItemsReq():
    def __init__(self, req):
        self.shopId = req['shopId'] if 'shopId' in req else None
        self.id = req['id'] if 'id' in req else None
        self.name = req['name'] if 'name' in req else None

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }


