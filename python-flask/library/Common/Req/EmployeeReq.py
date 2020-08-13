class CreateEmployeeReq():
    def __init__(self, req):
        self.identity_id = req['identity_id']
        self.account_id = req['account_id']
        self.last_name = req['last_name']
        self.first_name = req['first_name']
        self.phone = req['phone']
        self.birth_date = req['birth_date']
        self.hire_date = req['hire_date']
        self.address = req['address']
        self.gender = req['gender']
        self.image = req['image']
        self.basic_rate = req['basic_rate']
        self.note = req['note']
        self.delete_at = req['delete_at']


class UpdateEmployeeReq():
    def __init__(self, req):
        self.employee_id = req['employee_id']
        self.identity_id = req['identity_id']
        self.account_id = req['account_id']
        self.last_name = req['last_name']
        self.first_name = req['first_name']
        self.phone = req['phone']
        self.birth_date = req['birth_date']
        self.hire_date = req['hire_date']
        self.address = req['address']
        self.gender = req['gender']
        self.image = req['image']
        self.basic_rate = req['basic_rate']
        self.note = req['note']
        self.delete_at = req['delete_at']


class DeleteEmployeeReq():
    def __init__(self, req):
        self.employee_id = req['employee_id']


class SearchEmployeeByIdReq():
    def __init__(self, req):
        self.employee_id = req['employee_id']

class SearchEmployeeByIdentityIdReq():
    def __init__(self, req):
        self.identity_id = req['identity_id']


class SearchEmployeeByAccountIdReq():
    def __init__(self, req):
        self.account_id = req['account_id']

class SearchEmployeeByNameReq():
    def __init__(self, req):
        self.first_name = req['first_name']
        self.last_name = req['last_name']

class SearchEmployeeByPhoneReq():
    def __init__(self, req):
        self.phone = req['phone']