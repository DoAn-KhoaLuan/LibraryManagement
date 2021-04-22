class GetItemsByPageReq():
    def __init__(self, req):
        self.page = req['page'] if 'page' in req else None
        self.perPage = req['perPage'] if 'perPage' in req else None
        self.shopId = req['shopId'] if 'shopId' in req else None

class GetShopItemById():
    def __init__(self, req):
        self.id = req['id'] if 'id' in req else None
        self.shopId = req['shopId'] if 'shopId' in req else None

