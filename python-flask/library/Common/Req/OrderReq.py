class CreateOrderReq():
    def __init__(self, req):
        self.customer_id = req['customer_id'] if 'customer_id' in req else None
        self.employee_id = req['employee_id'] if 'employee_id' in req else None
        self.order_date = req['order_date'] if 'order_date' in req else None
        self.type = req['type'] if 'type' in req else None
        self.total = req['total'] if 'total' in req else None
        self.note = req['note'] if 'note' in req else None
        self.order_detail_list = req['order_detail_list'] if 'order_detail_list' in req else None
        self.delete_at = req['delete_at'] if 'delete_at' in req else None


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
