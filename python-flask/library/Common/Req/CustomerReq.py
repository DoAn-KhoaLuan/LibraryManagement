class CreateCustomerReq():
    def __init__(self, req):
        self.identity_id = req['identity_id']
        self.account_id = req['account_id']
        self.student_code = req['student_code']
        self.last_name = req['last_name']
        self.first_name = req['first_name']
        self.email = req['email']
        self.phone = req['phone']
        self.birth_date = req['birth_date']
        self.address = req['address']
        self.gender = req['gender']
        self.note = req['note']
        self.delete_at = req['delete_at']


class UpdateCustomerReq():
    def __init__(self, req):
        self.customer_id = req['customer_id']
        self.identity_id = req['identity_id']
        self.account_id = req['account_id']
        self.student_code = req['student_code']
        self.last_name = req['last_name']
        self.first_name = req['first_name']
        self.email = req['email']
        self.phone = req['phone']
        self.birth_date = req['birth_date']
        self.address = req['address']
        self.gender = req['gender']
        self.note = req['note']
        self.delete_at = req['delete_at']


class DeleteCustomerReq():
    def __init__(self, req):
        self.customer_id = req['customer_id']


class SearchCustomerByIdReq():
    def __init__(self, req):
        self.customer_id = req['customer_id']


class SearchCustomerByAccountIdReq():
    def __init__(self, req):
        self.customer_id = req['customer_id']


class SearchCustomerByIdentityIdReq():
    def __init__(self, req):
        self.identity_id = req['identity_id']


class SearchCustomerByAccountIdReq():
    def __init__(self, req):
        self.account_id = req['account_id']


class SearchCustomerByPhoneReq():
    def __init__(self, req):
        self.phone = req['phone']
