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

class LoginReq():
    def __init__(self, req):
        self.user_name = req['user_name']
        self.password = req['password']

class LoginRsp():
    def __init__(self, req):
        self.access_token = req['access_token'] if 'access_token' in req else None
        self.user_account = req['user_account'] if 'user_account' in req else None
        self.account = req['account'] if 'account' in req else None

    def serialize(self):
        return {
            "access_token": self.access_token.decode('utf-8'),
            "user_account": self.user_account,
            "account": self.account
        }

class SearchAccountsReq():
    def __init__(self, req):
        self.account_id = req['account_id'] if 'account_id' in req else None
        self.account_name = req['account_name'] if 'account_name' in req else None


class SendResetPasswordEmailReq():
    def __init__(self, req):
        self.email = req['email'] if 'email' in req else None


class ResetPasswordReq():
    def __init__(self, req):
        self.token = req['token'] if 'token' in req else None
        self.password = req['password'] if 'password' in req else None
