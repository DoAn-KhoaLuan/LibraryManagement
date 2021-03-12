class GetItemsByPageReq():
    def __init__(self, req):
        self.page = req['page']
        self.per_page = req['per_page']
