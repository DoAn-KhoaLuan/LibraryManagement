class CreateOrderReq():
    def __init__(self, req):
        self.sellerAccountId = req['sellerAccountId'] if 'sellerAccountId' in req else None
        self.buyerAccountId = req['buyerAccountId'] if 'buyerAccountId' in req else None
        self.total = req['order_date'] if 'order_date' in req else None
        self.type = req['type'] if 'type' in req else None
        self.note = req['note'] if 'note' in req else None
        self.shopId = req['shopId'] if 'shopId' in req else None
        self.orderDetailList = req['orderDetailList'] if 'orderDetailList' in req else None


class UpdateOrderReq():
    def __init__(self, req):
        self.order_id = req['order_id'] if "order_id" in req else None
        self.customer_id = req['customer_id'] if 'customer_id' in req else None
        self.employee_id = req['employee_id'] if 'employee_id' in req else None
        self.order_date = req['order_date'] if 'order_date' in req else None
        self.type = req['type'] if 'type' in req else None
        self.total = req['total'] if 'total' in req else None
        self.note = req['note'] if 'note' in req else None
        self.order_detail_list = req['order_detail_list'] if 'order_detail_list' in req else None
        self.delete_at = req['delete_at'] if 'delete_at' in req else None


class DeleteOrderReq():
    def __init__(self, req):
        self.order_id = req['order_id'] if "order_id" in req else None


class SearchOrdersReq():
    def __init__(self, req):
        self.order_id = req['order_id'] if "order_id" in req else None
        self.customer_id = req['customer_id'] if "customer_id" in req else None
        self.employee_id = req['employee_id'] if "employee_id" in req else None
        self.order_date = req['order_date'] if "order_date" in req else None


