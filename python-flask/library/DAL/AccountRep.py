from library import db
from library.Common.Req.AccountReq import CreateAccountReq, DeleteAccountReq
from library.Common.util import ConvertModelListToDictList
from library.DAL import models
from datetime import datetime
from library import bcrypt

def CreateAccount(req: CreateAccountReq):
    hashed_password = bcrypt.generate_password_hash(req.account_password,15)
    create_account = models.Accounts(account_name=req.account_name,
                                     account_password=hashed_password,
                                     note=req.note, delete_at=req.deleted_at, role_id=req.role_id)
    db.session.add(create_account)
    db.session.commit()
    return create_account.serialize()


def ValidateAccountName(acc_name: str):
    acc = models.Accounts.query.filter(models.Accounts.account_name == (acc_name)).first()
    return True if acc else False


def GetAccountsByPage(req):
    account_pagination = models.Accounts.query.paginate(page=req.page, per_page=req.per_page)
    has_next = account_pagination.has_next
    has_prev = account_pagination.has_prev
    accounts = ConvertModelListToDictList(account_pagination.items)
    return has_next, has_prev, accounts


def DeleteAccount(acc_info: DeleteAccountReq):
    deleted_account = models.Accounts.query.filter((models.Accounts.account_name == acc_info.account_name) | (
                models.Accounts.account_id == acc_info.account_id)).first()
    deleted_account.delete_at = datetime.now()
    db.session.add(deleted_account)
    db.session.commit()
    return acc_info
