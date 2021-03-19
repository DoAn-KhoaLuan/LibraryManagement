from datetime import datetime

# from flask_bcrypt import check_password_hash
# from sqlalchemy import or_
import hashlib

from library import db
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
# def DeleteAccount(acc_info: DeleteAccountReq):
#     deleted_account = models.Accounts.query.filter((models.Accounts.account_name == acc_info.account_name) | (
#             models.Accounts.account_id == acc_info.account_id)).first()
#     deleted_account.delete_at = datetime.now()
#     db.session.add(deleted_account)
#     db.session.commit()
#     return acc_info
#
#
def Authenticate(acc: LoginReq):
    account = models.Account.query.filter(models.Account.accountName == acc.accountName).first()
    if not account:
        raise ErrorRsp(code=400, message='Tài khoản không tồn tại', msg='Tài khoản không tồn tại')

    return account.serialize()


# def GetAccountByCustomerEmail(req):
#     customer_email = req.email
#     account = models.Customers.query.filter(models.Customers.email == customer_email).first().account.serialize()
#     return account
#
#
# def GetAccountByEmployeeEmail(req: SendResetPasswordEmailReq):
#     employee_email = req.email
#     account = models.Employees.query.filter(models.Employees.email == employee_email).first().account.serialize()
#     return account
#
#
# def ResetPassword(acc_id, password):
#     account = models.Accounts.query.get(int(acc_id))
#     account.account_password = hashlib.md5(password.encode('utf-8')).hexdigest()
#     db.session.commit()
#     return account.serialize()
#
#
# def ChangePassword(req: ChangePasswordReq):
#     account = models.Accounts.query.get(int(req.account_id))
#     hashed_new_password = str(hashlib.md5(req.new_password.strip().encode("utf-8")).hexdigest())
#     hashed_current_password = str(hashlib.md5(req.current_password.strip().encode("utf-8")).hexdigest())
#
#     if account.account_password == hashed_current_password:
#         account.account_password = hashed_new_password
#         db.session.commit()
#     else:
#         raise ErrorRsp(code=400, message='Mật khẩu không chính xác', msg="Mật khẩu không chính xác")
#
#     return account.serialize()
#
#
# def CreateCustomerAccount(req: CreateCustomerAccountReq):
#     is_exist_account_name_customer = models.Accounts.query.filter(
#         models.Accounts.account_name == req.account_name).first()
#     is_exist_email_phone_customer = models.Customers.query.filter(or_(models.Customers.email == req.email,
#                                                                       models.Customers.phone == req.phone)).first()
#     if is_exist_account_name_customer:
#         raise ErrorRsp(code=400, message='Tài khoản tồn tại', msg='Tài khoản tồn tại')
#
#     hashed_password = hashlib.md5(req.account_password.encode('utf-8')).hexdigest()
#     create_account = models.Accounts(account_name=req.account_name,
#                                      account_password=hashed_password, role_id=req.role_id)
#
#     db.session.begin_nested()
#     db.session.add(create_account)
#     db.session.commit()
#
#     if is_exist_email_phone_customer:
#         db.session.rollback()
#         raise ErrorRsp(code=400, message='số điện thoại, chứng minh nhân dân hoặc email đẫ tồn tại',
#                        msg='số điện thoại, chứng minh nhân dânhoặc email đẫ tồn tại')
#     create_customer = models.Customers(identity_id=req.identity_id,
#                                        account_id=create_account.account_id,
#                                        last_name=req.last_name,
#                                        first_name=req.first_name,
#                                        phone=req.phone,
#                                        student_code=req.student_code,
#                                        birth_date=req.birth_date,
#                                        address=req.address,
#                                        gender=req.gender,
#                                        email=req.email)
#
#     db.session.add(create_customer)
#     db.session.commit()
#
#     return create_account.serialize(), create_customer.serialize()
#
#
# def CreateEmployeeAccount(req: CreateEmployeeAccountReq):
#     is_exist_account_name_employee = models.Accounts.query.filter(models.Accounts.account_name == req.account_name).first()
#     is_exist_email_phone_employee = models.Employees.query.filter(or_(models.Employees.email == req.email,
#                                                                       models.Employees.phone == req.phone,
#                                                                       models.Employees.identity_id == req.identity_id)).first()
#     if is_exist_account_name_employee:
#         raise ErrorRsp(code=400, message='Tài khoản tồn tại', msg='Tài khoản tồn tại')
#
#     hashed_password = hashlib.md5(req.account_password.encode('utf-8')).hexdigest()
#     create_account = models.Accounts(account_name=req.account_name,
#                                      account_password=hashed_password,
#                                      note=req.note, role_id=req.role_id)
#     db.session.begin_nested()
#     db.session.add(create_account)
#     db.session.commit()
#     if is_exist_email_phone_employee:
#         db.session.rollback()
#         raise ErrorRsp(code=400, message='số điện thoại, chứng minh nhân dân hoặc email đẫ tồn tại',
#                        msg='số điện thoại, chứng minh nhân dân hoặc email đẫ tồn tại')
#     create_employee = models.Employees(identity_id=req.identity_id,
#                                        account_id=create_account.account_id,
#                                        last_name=req.last_name,
#                                        first_name=req.first_name,
#                                        phone=req.phone,
#                                        email=req.email,
#                                        birth_date=req.birth_date,
#                                        hire_date=req.hire_date,
#                                        address=req.address,
#                                        gender=req.gender,
#                                        image=req.image,
#                                        basic_rate=req.basic_rate,
#                                        note=req.note)
#
#     db.session.add(create_employee)
#     db.session.commit()
#
#     return create_account.serialize(), create_employee.serialize()

def getAccountById(id):
    accountModel = models.Account.query.filter(models.Account.id == id).first();
    return accountModel.serialize()
