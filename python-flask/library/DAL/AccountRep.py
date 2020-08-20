from flask_bcrypt import check_password_hash
from sqlalchemy import or_
import hashlib
from library import db
from library.Common.Req.AccountReq import CreateAccountReq, DeleteAccountReq, LoginReq, SendResetPasswordEmailReq
from library.Common.Rsp.SingleRsp import ErrorRsp
from library.Common.util import ConvertModelListToDictList
from library.DAL import models
from datetime import datetime
from library import bcrypt

def CreateAccount(req: CreateAccountReq):
    hashed_password = hashlib.md5(req.account_password.encode('utf-8')).hexdigest()
    create_account = models.Accounts(account_name=req.account_name,
                                     account_password=hashed_password,
                                     note=req.note, delete_at=req.deleted_at, role_id=req.role_id)
    db.session.add(create_account)
    db.session.commit()
    return create_account.serialize()


def ValidateAccountName(acc_name: str):
    acc = models.Accounts.query.filter(models.Accounts.account_name == (acc_name) and models.Accounts.delete_at == None).first()
    return True if acc else False


def GetAccountsByPage(req):
    account_pagination = models.Accounts.query.paginate(page=req.page, per_page=req.per_page)
    has_next = account_pagination.has_next
    has_prev = account_pagination.has_prev
    accounts = ConvertModelListToDictList(account_pagination.items)
    return has_next, has_prev, accounts

def SearchAccounts(acc_info):
    model_accounts = models.Accounts.query.filter(or_(models.Accounts.account_id == acc_info.account_id,
                                                models.Accounts.account_name == acc_info.account_name,
                                               )).all()
    accounts = ConvertModelListToDictList(model_accounts)
    return accounts

def DeleteAccount(acc_info: DeleteAccountReq):
    deleted_account = models.Accounts.query.filter((models.Accounts.account_name == acc_info.account_name) | (
                models.Accounts.account_id == acc_info.account_id)).first()
    deleted_account.delete_at = datetime.now()
    db.session.add(deleted_account)
    db.session.commit()
    return acc_info

def Authenticate(acc_info: LoginReq):
    account = models.Accounts.query.filter_by(account_name=acc_info.user_name).first()
    if not account:
        raise ErrorRsp(code=400, message='Tài khoản không tồn tại')

    if(str(hashlib.md5(acc_info.password.encode('utf-8')).hexdigest()) != account.account_password):
        raise ErrorRsp(code=400, message='Mật khẩu không chính xác')
    return account.serialize()

def GetAccountByCustomerEmail(req):
    customer_email = req.email
    account = models.Customers.query.filter(models.Customers.email == customer_email).first().account.serialize()
    return account


def GetAccountByEmployeeEmail(req: SendResetPasswordEmailReq):
    employee_email = req.email
    account = models.Employees.query.filter(models.Employees.email == employee_email).first().account.serialize()
    return account

def ChangePassword(acc_id, password):
    account = models.Accounts.query.get(acc_id)
    account.account_password = password
    db.session.commit()
    return account.serialize()
