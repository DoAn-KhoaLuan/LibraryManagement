import json
from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import request, jsonify

from library import app, smtp
from library.BLL import AccountSvc
from library.Common.Req.AccountReq import CreateAccountReq, DeleteAccountReq, LoginReq, LoginRsp, SearchAccountsReq, \
    SendResetPasswordEmailReq, ResetPasswordReq
from library.Common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.Common.Rsp.AccountRsp import SearchAccountsRsp
from library.Common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from library.Common.Rsp.SingleRsp import ErrorRsp
from library.auth import token_required
from library.DAL import EmployeeRep, CustomerRep, AccountRep
import smtplib
from email.message import EmailMessage
@app.route('/admin/account-management/create-account', methods=['POST'])
def CreateAccount() -> CreateAccountReq:
    req = CreateAccountReq(request.json)
    result = AccountSvc.CreateAccount(req)
    return result

@app.route('/admin/account-management/get-accounts', methods=['POST'])
# @token_required
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

@app.route('/admin/account-management/search-accounts', methods=['POST'])
def SearchAccounts():
    req = SearchAccountsReq(request.json)
    accounts = AccountSvc.SearchAccounts(req)
    res = SearchAccountsRsp(accounts).serialize()
    return jsonify(res)

@app.route('/admin/account-management/login', methods=['POST'])
def LoginAccount():
    try:
        req = LoginReq(request.json)
        result = AccountSvc.AuthenticateUser(req)
        res = LoginRsp(result).serialize()
        return jsonify(res)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8'), 401



@app.route('/send-reset-password-email-customer', methods=['POST'])
def SendResetPasswordEmailCustomer():
    req = SendResetPasswordEmailReq(request.json)
    result = AccountSvc.SendResetPasswordEmailCustomer(req)
    return result

@app.route('/send-reset-password-email-employee', methods=['POST'])
def SendResetPasswordEmailEmployee():
    req = SendResetPasswordEmailReq(request.json)
    result = AccountSvc.SendResetPasswordEmailEmployee(req)
    return result


@app.route('/reset_password', methods=['POST'])
def resetPassword():
    req = ResetPasswordReq(request.json)
    result = AccountSvc.ResetPassword(req)
    return jsonify(result)

