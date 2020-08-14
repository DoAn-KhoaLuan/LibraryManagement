class CreateOrderReq():
    def __init__(self, req):
        self.customer_id = req['customer_id']
        self.employee_id = req['employee_id']
        self.order_date = req['order_date']
        self.type = req['type']
        self.total = req['total']
        self.note = req['note']
        self.delete_at = req['delete_at']


class UpdateOrderReq():
    def __init__(self, req):
        self.order_id = req['order_id']
        self.customer_id = req['customer_id']
        self.employee_id = req['employee_id']
        self.order_date = req['order_date']
        self.type = req['type']
        self.total = req['total']
        self.note = req['note']
        self.delete_at = req['delete_at']


class DeleteOrderReq():
    def __init__(self, req):
        self.order_id = req['order_id']


class SearchOrderByOrderIdReq():
    def __init__(self, req):
        self.order_id = req['order_id']


class SearchOrderByCustomerIdReq():
    def __init__(self, req):
        self.customer_id = req['customer_id']


class SearchOrderByEmployeeIdReq():
    def __init__(self, req):
        self.employee_id = req['employee_id']


class SearchOrderByOrderDateReq():
    def __init__(self, req):
        self.order_date = req['order_date']
