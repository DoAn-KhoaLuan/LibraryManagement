class CreateOrderDetailReq():
    def __init__(self, req):
        self.order_id = req['order_id']
        self.book_id = req['book_id']
        self.retail_price = req['retail_price']
        self.quantity = req['quantity']
        self.discount = req['discount']
        self.total = req['total']
        self.note = req['note']
        self.delete_at = req['delete_at']
