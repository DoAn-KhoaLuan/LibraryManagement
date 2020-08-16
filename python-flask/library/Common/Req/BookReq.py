class CreateBookReq(object):
    def __init__(self, req):
        self.book_name = req['book_name']
        self.supplier_id = req['supplier_id']
        self.category_id = req['category_id']
        self.author_id = req['author_id']
        self.old_amount = req['old_amount']
        self.new_amount = req['new_amount']
        self.image = req['image']
        self.page_number = req['page_number']
        self.description = req['description']
        self.cost_price = req['cost_price']
        self.retail_price = req['retail_price']
        self.discount = req['discount']
        self.ranking = req['ranking']


class DeleteBookByIdReq():
    def __init__(self, req):
        self.book_id = req['book_id']


class UpdateBookReq():
    def __init__(self, req):
        self.book_id = req['book_id']
        self.book_name = req['book_name']
        self.supplier_id = req['supplier_id']
        self.category_id = req['category_id']
        self.author_id = req['author_id']
        self.old_amount = req['old_amount']
        self.new_amount = req['new_amount']
        self.image = req['image']
        self.page_number = req['page_number']
        self.description = req['description']
        self.cost_price = req['cost_price']
        self.retail_price = req['retail_price']
        self.discount = req['discount']
        self.ranking = req['ranking']
        self.ranking = req['ranking']


class SearchBookReq:
    def __init__(self, req):
        self.keyword = req['keyword'] if 'keyword' in req else None
