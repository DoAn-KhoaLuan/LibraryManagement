import jwt
from datetime import datetime, timedelta
from library import app
from library.Common.Req.AccountReq import CreateAccountReq, DeleteAccountReq, LoginReq
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
