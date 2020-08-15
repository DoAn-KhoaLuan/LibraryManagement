class CreateAccountReq():
    def __init__(self, req):
        self.role_id = req['role_id'] if 'role_id' in req else None
        self.account_name = req['account_name'] if 'account_name' in req else None
        self.account_password = req['account_password'] if 'account_password' in req else None
        self.confirm_account_password =  req['confirm_account_password'] if 'confirm_account_password' in req else None
        self.deleted_at = req['deleted_at'] if 'deleted_at' in req else None
        self.note = req['note'] if 'note' in req else None


class DeleteAccountReq():
    def __init__(self, req):
        self.account_id = req['account_id'] if 'account_id' in req else ''
        self.account_name = req['account_name'] if 'account_name' in req else ''

    def serialize(self):
        return {
            "account_name": self.account_name,
            "account_id": self.account_id
        }

