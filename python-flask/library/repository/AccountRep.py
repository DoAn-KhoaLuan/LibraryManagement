from builtins import print
from datetime import datetime

# from flask_bcrypt import check_password_hash
# from sqlalchemy import or_
import hashlib

import jwt

from library import db, app
from library.miration import models
from library.common.Req.AccountReq import *
#     ChangePasswordReq, CreateCustomerAccountReq, CreateEmployeeAccountReq
# from library.common.Rsp.SingleRsp import ErrorRsp
# from library.common.util import ConvertModelListToDictList
# from datetime import datetime
# from library import bcrypt
from library.common.Rsp.SingleRsp import ErrorRsp
from library.miration.models import AccountRole


def CreateAccount(req: CreateAccountReq):
    hashedPassword = hashlib.md5(req.accountPassword.encode('utf-8')).hexdigest()
    createAccount = models.Account(
        provinceId= req.provinceId,
        districtId= req.districtId,
        wardId= req.wardId,
        address= req.address,
        roleName= AccountRole.USER,
        accountName= req.accountName,
        accountPassword= hashedPassword,
        lastName= req.lastName,
        firstName= req.firstName,
        phone= req.phone,
        email= req.email,
        birthDate= req.birthDate,
        imageUrl= req.imageUrl,
        note= req.note,
        createAt = datetime.now()
    )
    db.session.add(createAccount)
    db.session.commit()
    return createAccount.serialize()
#
#
def ValidateAccountName(accountName: str):
    acc = models.Account.query.filter(
        models.Account.accountName == accountName and models.Accounts.delete_at is None).first()
    return True if acc else False

# def GetAccountsByPage(req):
#     account_pagination = models.Accounts.query.filter(models.Accounts.delete_at == None).paginate(page=req.page,
#                                                                                                   per_page=req.per_page)
#     hasNext = account_pagination.hasNext
#     hasPrev = account_pagination.hasPrev
#     accounts = ConvertModelListToDictList(account_pagination.items)
#     return hasNext, hasPrev, accounts
#
#
# def SearchAccounts(acc_info):
#     model_accounts = models.Accounts.query.filter(or_(models.Accounts.account_id == acc_info.account_id,
#                                                       models.Accounts.account_name == acc_info.account_name,
#                                                       )).all()
#     accounts = ConvertModelListToDictList(model_accounts)
#     return accounts
#
#
def deleteAccount(account):
    deleteAccount = models.Account.query.filter((models.Account.id == account['shop']['id'])).first()
    print(deleteAccount)
    deleteAccount.deleteAt = datetime.now()
    db.session.add(deleteAccount)
    db.session.commit()
    return deleteAccount.serialize()
#
#
def authenticate(acc: LoginReq):
    account = models.Account.query.filter(models.Account.accountName == acc.accountName).first()
    hashedCurrentPassword = str(hashlib.md5(acc.accountPassword.strip().encode("utf-8")).hexdigest())

    if not account:
        raise ErrorRsp(code=400, message='Tài khoản không tồn tại', msg='Tài khoản không tồn tại')

    if account.accountPassword != hashedCurrentPassword:
        raise ErrorRsp(code=400, message='Mật khẩu không chính xác', msg='Mật khẩu không chính xác')

    if account.deleteAt != None:
        raise ErrorRsp(code=400, message='Tài khoản đã bị vô hiệu hóa', msg='Tài khoản đã bị vô hiệu hóa')


    return account.serialize()


# def GetAccountByCustomerEmail(req):
#     customer_email = req.email
#     account = models.Customers.query.filter(models.Customers.email == customer_email).first().account.serialize()
#     return account
#
#
def getAccountByEmail(email):
    account = models.Account.query.filter(models.Account.email == email).first()
    return account.serialize()
#
#
def changePassword(req: ChangePasswordReq):
    account = models.Account.query.get(int(req.id))
    hashedNewPassword = str(hashlib.md5(req.newPassword.strip().encode("utf-8")).hexdigest())
    hashedCurrentPassword = str(hashlib.md5(req.currentPassword.strip().encode("utf-8")).hexdigest())

    if account.accountPassword == hashedCurrentPassword:
        account.accountPassword = hashedNewPassword
        db.session.commit()
    else:
        raise ErrorRsp(code=400, message='Mật khẩu không chính xác', msg="Mật khẩu không chính xác")

    return account.serialize()
#
#
def resetPassword(req: ResetPasswordReq):
    payload = jwt.decode(req.token, app.config['SECRET_KEY'])
    accountId = payload["accountId"]
    account = models.Account.query.get(int(accountId))

    hashedNewPassword = str(hashlib.md5(req.password.strip().encode("utf-8")).hexdigest())

    account.accountPassword = hashedNewPassword
    db.session.commit()

    return account.serialize()


def getAccountById(id):
    accountModel = models.Account.query.filter(models.Account.id == id).first()
    return accountModel.serialize()
