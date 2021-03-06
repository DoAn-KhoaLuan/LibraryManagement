# from email.message import EmailMessage
#
from email.message import EmailMessage

import jwt
from datetime import datetime, timedelta
#
from flask import jsonify
#
from library import app, smtp
#
# from library.common.Req.AccountReq import CreateAccountReq, DeleteAccountReq, LoginReq, SendResetPasswordEmailReq, \
#     ResetPasswordReq, ChangePasswordReq
#
# from library.common.Req.CustomerReq import SearchCustomersReq
#
# from library.common.Req.EmployeeReq import SearchEmployeesReq
#
# from library.common.Rsp.SingleRsp import ErrorRsp
#
from library.common.Req.AccountReq import *
from library.common.Rsp.SingleRsp import ErrorRsp
from library.repository import AccountRep
#
#
def createAccount(req: CreateAccountReq):
    is_account_existed = AccountRep.ValidateAccountName(req.accountName)
    if (is_account_existed):
        return jsonify({'msg': "Tài khoản đã tồn tại"}), 401
    else:
        res = AccountRep.CreateAccount(req)
        return res
#
#
# def GetAccountsByPage(req):
#     hasNext, hasPrev, accounts = AccountRep.GetAccountsByPage(req)
#     result = {
#         "hasNext": hasNext,
#         "hasPrev": hasPrev,
#         "accounts": accounts
#     }
#     return result
#
#
def deleteAccount(account):
    res = AccountRep.deleteAccount(account)
    return res
#
#
# def SearchAccounts(acc_info):
#     accounts = AccountRep.SearchAccounts(acc_info)
#     info_accounts = []
#     for account in accounts:
#         user_info = {}
#         if (account['role']['role_id'] == 3):  # customer
#             search_customer_req = SearchCustomersReq({'account_id': account['account_id']})
#             user_info = CustomerRep.SearchCustomers(search_customer_req)
#
#         if (account['role']['role_id'] == 1 or account['role']['role_id'] == 2):  # admin, manager
#             search_employee_req = SearchEmployeesReq({'account_id': account['account_id']})
#             user_info = EmployeeRep.SearchEmployees(search_employee_req)
#
#         account_info = user_info[0] if user_info else {'account': account}
#         info_accounts.append(account_info)
#
#     return info_accounts
#
#

def extractToken(token):
    payload = jwt.decode(token, app.config['SECRET_KEY'])
    accountId = payload["accountId"]
    account = AccountRep.getAccountById(accountId)
    return account


def sessionInfo(token):
    invalid_msg = {
        'message': 'Token không hợp lệ.',
        'authenticated': False
    }
    expired_msg = {
        'message': 'Token hết hạn sử dụng.',
        'authenticated': False
    }
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'])
        accountId = payload["accountId"]
        account = AccountRep.getAccountById(accountId)
        result = {
            'accessToken': token,
            'account': account,
        }
        return result

    except jwt.ExpiredSignatureError:
        return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
    except (jwt.InvalidTokenError) as e:
        return jsonify(invalid_msg), 401


def login(acc: LoginReq):
    try:
        account = AccountRep.authenticate(acc)

        secrectKey = app.config['SECRET_KEY']
        payload = {
            'accountId': account['id'],
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=3600)
        }
        accessToken = jwt.encode(payload, secrectKey)
        result = {
            'accessToken': accessToken,
            'account': account,
        }

        return result
    except ErrorRsp as e:
        raise e


# def SendResetPasswordEmailCustomer(req: SendResetPasswordEmailReq):
#     smtp.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
#     account = AccountRep.GetAccountByCustomerEmail(req)
#     secect_key = app.config['SECRET_KEY']
#     payload = {
#         'account_id': account['account_id'],
#         'iat': datetime.utcnow(),
#         'exp': datetime.utcnow() + timedelta(minutes=30)
#     }
#     reset_email_token = jwt.encode(payload, secect_key).decode('utf-8')
#
#     msg = EmailMessage()
#     msg['Subject'] = 'Khôi phục mật khẩu Thư quán Đại học Mở TPHCM'
#     msg['From'] = app.config['MAIL_USERNAME']
#     msg['To'] = req.email
#     msg.set_content(
#         f'''    Gửi {app.config['MAIL_USERNAME']},
#     Bạn (hoặc một ai đó) đang muốn khôi phục mật khẩu của tài khoản shinichi24567@gmail.com-01-test.
#     Nếu là bạn, hãy bấm vào liên kết bên dưới để khôi phục mật khẩu: (có hiệu lực trong 24 giờ)
#
#     http://localhost:4200/reset-password?token={reset_email_token}
#     Nếu không phải bạn, hãy bỏ qua email này.
#
#     Đội ngũ quản lý thư quán Đại học Mở TPHCM!
# ''')
#     smtp.send_message(msg)
#     return " Vui lòng kiểm tra email để reset mật khẩu"
#
#
def sendResetPasswordEmail(req: SendResetPasswordEmailReq):
    smtp.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    account = AccountRep.getAccountByEmail(req.email)
    secect_key = app.config['SECRET_KEY']
    payload = {
        'accountId': account['id'],
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    resetEmailToken = jwt.encode(payload, secect_key).decode('utf-8')

    msg = EmailMessage()
    msg['Subject'] = 'Khôi phục mật khẩu Hatubo'
    msg['From'] = app.config['MAIL_USERNAME']
    msg['To'] = req.email
    msg.set_content(
        f'''    Gửi {account['firstName']} {account['lastName']},
    Bạn (hoặc một ai đó) đang muốn khôi phục mật khẩu của tài khoản {account['accountName']}.
    Nếu là bạn, hãy bấm vào liên kết bên dưới để khôi phục mật khẩu: (có hiệu lực trong 24 giờ)

    http://localhost:4200/reset-password?token={resetEmailToken}
    Nếu không phải bạn, hãy bỏ qua email này.

    Đội ngũ quản lý Hatubo!
''')
    smtp.send_message(msg)
    return {msg: 'Vui lòng kiểm tra email để reset mật khẩu'}
#
#
def changePassword(req: ChangePasswordReq):
    try:
        result = AccountRep.changePassword(req)
        return result
    except ErrorRsp as e:
        raise e


def resetPassword(req: ResetPasswordReq):
    try:
        return AccountRep.resetPassword(req)
    except ErrorRsp as e:
        raise e
#
#
# def CreateCustomerAccount(req):
#     create_customer_account = AccountRep.CreateCustomerAccount(req)
#     create_conversation_request = {
#         'customer_account_id': create_customer_account[0]['account_id']
#     }
#     _ = MessageRep.CreateConversation(create_conversation_request)
#     return create_customer_account
#
#
# def CreateEmployeeAccount(req):
#     create_employee_account = AccountRep.CreateEmployeeAccount(req)
#     return create_employee_account
