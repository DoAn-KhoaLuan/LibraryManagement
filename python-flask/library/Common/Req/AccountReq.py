class CreateAccountReq():
    def __init__(self, req):
        self.role_id = req['role_id']
        self.account_name = req['account_name']
        self.account_password = req['account_password']
        self.confirm_account_password = req['confirm_account_password']
        self.note = req['note']


class DeleteAccountReq():
    def __init__(self, req):
        self.account_id = req['account_id'] if 'account_id' in req else ''
        self.account_name = req['account_name'] if 'account_name' in req else ''

    def serialize(self):
        return {
            "account_name": self.account_name,
            "account_id": self.account_id
        }

