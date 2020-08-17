from email.message import EmailMessage

import jwt
from datetime import datetime, timedelta
from library import app, smtp
from library.Common.Req.AccountReq import CreateAccountReq, DeleteAccountReq, LoginReq, SendResetPasswordEmailReq, \
    ResetPasswordReq
from library.Common.Rsp.SingleRsp import ErrorRsp
from library.DAL import AccountRep


def CreateAccount(req):
    is_account_existed = AccountRep.ValidateAccountName(req.account_name)
    if(is_account_existed):
        return "Tài khoản đã tồn tại"
    else:
        res = AccountRep.CreateAccount(req)
        return res

def GetAccountsByPage(req):
    has_next, has_prev, accounts = AccountRep.GetAccountsByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "accounts": accounts
    }
    return result

def DeleteAccount(req: DeleteAccountReq):
    res = AccountRep.DeleteAccount(req)
    return res

def SearchAccounts(acc_info):
    accounts = AccountRep.SearchAccounts(acc_info)
    return accounts

def AuthenticateUser(acc: LoginReq):
    try:
        account = AccountRep.Authenticate(acc)
        secect_key = app.config['SECRET_KEY']
        payload = {
            'account_id': account.account_id,
            'iat':datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }
        access_token = jwt.encode(payload, secect_key)
        result = {
            'access_token': access_token
        }
        return result
    except ErrorRsp as e:
        raise e

def SendResetPasswordEmailCustomer(req: SendResetPasswordEmailReq):
    smtp.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    account = AccountRep.GetAccountByCustomerEmail(req)
    secect_key = app.config['SECRET_KEY']
    payload = {
        'account_id': account['account_id'],
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    reset_email_token = jwt.encode(payload, secect_key).decode('utf-8')

    msg = EmailMessage()
    msg['Subject'] = 'Khôi phục mật khẩu Thư quán Đại học Mở TPHCM'
    msg['From'] = app.config['MAIL_USERNAME']
    msg['To'] = req.email
    msg.set_content(
        f'''    Gửi {app.config['MAIL_USERNAME']},
    Bạn (hoặc một ai đó) đang muốn khôi phục mật khẩu của tài khoản shinichi24567@gmail.com-01-test.
    Nếu là bạn, hãy bấm vào liên kết bên dưới để khôi phục mật khẩu: (có hiệu lực trong 24 giờ)

    {reset_email_token}
    Nếu không phải bạn, hãy bỏ qua email này.

    Đội ngũ quản lý thư quán Đại học Mở TPHCM!
''')
    smtp.send_message(msg)
    return " Vui lòng kiểm tra email để reset mật khẩu"

def SendResetPasswordEmailEmployee(req: SendResetPasswordEmailReq):
    smtp.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    account = AccountRep.GetAccountByEmployeeEmail(req)
    secect_key = app.config['SECRET_KEY']
    payload = {
        'account_id': account['account_id'],
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    reset_email_token = jwt.encode(payload, secect_key).decode('utf-8')

    msg = EmailMessage()
    msg['Subject'] = 'Khôi phục mật khẩu Thư quán Đại học Mở TPHCM'
    msg['From'] = app.config['MAIL_USERNAME']
    msg['To'] = req.email
    msg.set_content(
        f'''    Gửi {app.config['MAIL_USERNAME']},
    Bạn (hoặc một ai đó) đang muốn khôi phục mật khẩu của tài khoản shinichi24567@gmail.com-01-test.
    Nếu là bạn, hãy bấm vào liên kết bên dưới để khôi phục mật khẩu: (có hiệu lực trong 24 giờ)

    {reset_email_token}
    Nếu không phải bạn, hãy bỏ qua email này.

    Đội ngũ quản lý thư quán Đại học Mở TPHCM!
''')
    smtp.send_message(msg)
    return " Vui lòng kiểm tra email để reset mật khẩu"

def ResetPassword(req: ResetPasswordReq):
    payload = jwt.decode(req.token, app.config['SECRET_KEY'])
    account_id = payload['account_id']
    result = AccountRep.ChangePassword(account_id, req.password)
    return result
