class GetItemsByPageReq():
    def __init__(self, req):
        self.page = req['page']
        self.per_page = req['per_page']


class SearchItemsReq():
    def __init__(self, req):
        self.account_id = req['account_id'] if 'account_id' in req else None
        self.account_name = req['account_name'] if 'account_name' in req else None
        self.role_id = req['role_id'] if 'role_id' in req else None
        self.book_id = req['book_id'] if 'book_id' in req else None
        self.id = req['id'] if 'id' in req else None
        self.book_name = req['book_name'] if 'book_name' in req else None
        self.author_id = req['author_id'] if 'author_id' in req else 0
        self.category_id = req['category_id'] if 'category_id' in req else 0
        self.supplier_id = req['supplier_id'] if 'supplier_id' in req else 0
