class CreateAccountRsp():
    def __init__(self, req):
        self.account_name = req.account_name
        self.role_id = req.role_id

    def serialize(self):
        return {
            "account_name": self.account_name,
            "role_id": self.role_id,
        }

class SessionInfoRsp():
    def __init__(self, req):
        self.accessToken = req['accessToken'] if 'accessToken' in req else None
        self.account = req['account'] if 'account' in req else None

    def serialize(self):
        return {
            "accessToken": self.accessToken,
            "account": self.account
        }

class SearchAccountsRsp():
    def __init__(self, accounts):
        self.accounts = accounts
    def serialize(self):
        return {
            "accounts": self.accounts,
        }
