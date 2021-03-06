class CreateAccountReq():
    def __init__(self, req):
        self.provinceId = req['provinceId'] if 'provinceId' in req else None
        self.districtId = req['districtId'] if 'districtId' in req else None
        self.wardId = req['wardId'] if 'wardId' in req else None
        self.address = req['address'] if 'address' in req else None
        self.accountName = req['accountName'] if 'accountName' in req else None
        self.accountPassword = req['accountPassword'] if 'accountPassword' in req else None
        self.lastName = req['lastName'] if 'lastName' in req else None
        self.firstName = req['firstName'] if 'firstName' in req else None
        self.phone = req['phone'] if 'phone' in req else None
        self.email = req['email'] if 'email' in req else None
        self.birthDate = req['birthDate'] if 'birthDate' in req else None
        self.imageUrl = req['imageUrl'] if 'imageUrl' in req else None
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
        self.accountName = req['accountName']
        self.accountPassword = req['accountPassword']


class LoginRsp():
    def __init__(self, req):
        self.accessToken = req['accessToken'] if 'accessToken' in req else None
        self.account = req['account'] if 'account' in req else None

    def serialize(self):
        return {
            "accessToken": self.accessToken.decode('utf-8'),
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


class ChangePasswordReq():
    def __init__(self, req):
        self.id = req['accountId'] if 'accountId' in req else None
        self.currentPassword = req['currentPassword'] if 'currentPassword' in req else None
        self.newPassword = req['newPassword'] if 'newPassword' in req else None


class CreateCustomerAccountReq():
    def __init__(self, req):
        # account
        self.account_name = req['account_name'] if 'account_name' in req else None
        self.role_id = req['role_id'] if 'role_id' in req else None
        self.account_password = req['account_password'] if 'account_password' in req else None
        # customer
        self.identity_id = req['identity_id'] if 'identity_id' in req else None
        self.account_id = req['account_id'] if 'account_id' in req else None
        self.student_code = req['student_code'] if 'student_code' in req else None
        self.last_name = req['last_name'] if 'last_name' in req else None
        self.first_name = req['first_name'] if 'first_name' in req else None
        self.email = req['email'] if 'email' in req else None
        self.phone = req['phone'] if 'phone' in req else None
        self.birth_date = req['birth_date'] if 'birth_date' in req else None
        self.address = req['address'] if 'address' in req else None
        self.gender = req['gender'] if 'gender' in req else None


class CreateEmployeeAccountReq():
    def __init__(self, req):
        # account
        self.account_name = req['account_name'] if 'account_name' in req else None
        self.role_id = req['role_id'] if 'role_id' in req else None
        self.account_password = req['account_password'] if 'account_password' in req else None
        # Employee
        self.identity_id = req['identity_id'] if 'identity_id' in req else None
        self.last_name = req['last_name'] if 'last_name' in req else None
        self.first_name = req['first_name'] if 'first_name' in req else None
        self.phone = req['phone'] if 'phone' in req else None
        self.email = req['email'] if 'email' in req else None
        self.birth_date = req['birth_date'] if 'birth_date' in req else None
        self.hire_date = req['hire_date'] if 'hire_date' in req else None
        self.address = req['address'] if 'address' in req else None
        self.gender = req['gender'] if 'gender' in req else None
        self.image = req['image'] if 'image' in req else None
        self.basic_rate = req['basic_rate'] if 'basic_rate' in req else None
        self.note = req['note'] if 'note' in req else None

