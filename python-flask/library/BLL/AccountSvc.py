from library.Common.Req.AccountReq import CreateAccountReq, DeleteAccountReq
from library.Common.Rsp.SingleRsp import ErrorRsp
from library.DAL import AccountRep


def CreateAccount(req):
    # is_account_existed = AccountRep.ValidateAccountName(req.account_name)
    # if(is_account_existed):
    #     return "sadsa"
    # else:
    #     print('svcc')
    #     return res
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
