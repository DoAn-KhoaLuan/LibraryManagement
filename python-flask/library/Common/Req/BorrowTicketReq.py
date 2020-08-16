class CreateBorrowTicketReq():
    def __init__(self, req):
        self.customer_id = req['customer_id']
        self.employee_id = req['employee_id']
        self.quantity = req['quantity']
        self.borrow_date = req['borrow_date']
        self.appointment_date = req['appointment_date']
        self.return_date = req['return_date']
        self.status = req['status']
        self.delete_at = req['delete_at']
        self.note = req['note']


class UpdateBorrowTicketReq():
    def __init__(self, req):
        self.borrow_ticket_id = req['borrow_ticket_id']
        self.customer_id = req['customer_id']
        self.employee_id = req['employee_id']
        self.quantity = req['quantity']
        self.borrow_date = req['borrow_date']
        self.appointment_date = req['appointment_date']
        self.return_date = req['return_date']
        self.status = req['status']
        self.delete_at = req['delete_at']
        self.note = req['note']


class DeleteBorrowTicketReq():
    def __init__(self, req):
        self.borrow_ticket_id = req['borrow_ticket_id']


class SearchBorrowTicketReq():
    def __init__(self, req):
        self.keyword = req['keyword'] if 'keyword' in req else None