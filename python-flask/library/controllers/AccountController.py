from flask import request, jsonify

from library import app
from library.BLL import AccountSvc
from library.Common.Req.AccountReq import CreateAccountReq, DeleteAccountReq
from library.Common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.Common.Rsp.AccountRsp import CreateAccountRsp
from library.Common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp


@app.route('/admin/account-management/create-account', methods=['POST'])
def CreateAccount():
    req = CreateAccountReq(request.json)
    result = AccountSvc.CreateAccount(req)
    return result

@app.route('/admin/account-management/get-accounts', methods=['POST'])
def GetAccounts():
        req = GetItemsByPageReq(request.json)
        result = AccountSvc.GetAccountsByPage(req)
        res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                                items=result['accounts']).serialize()
        return jsonify(res)


@app.route('/admin/account-management/delete-account', methods=['POST'])
def DeleteAccount():
    req = DeleteAccountReq(request.json)
    res = AccountSvc.DeleteAccount(req)
    return jsonify(res.serialize())
