# import json
# from datetime import datetime, timedelta
# from functools import wraps
#
# import jwt
# from flask import request, jsonify
#
import json
from flask import request, jsonify

from library import app
from library.auth import owner_required, user_required
from library.common.Rsp.AccountRsp import SessionInfoRsp
from library.common.Rsp.SingleRsp import ErrorRsp
from library.service import AccountSvc
# from library.common.Req.AccountReq import CreateAccountReq, DeleteAccountReq, LoginReq, LoginRsp, SearchAccountsReq, \
#     SendResetPasswordEmailReq, ResetPasswordReq, ChangePasswordReq, CreateCustomerAccountReq, CreateEmployeeAccountReq
# from library.common.Req.GetItemsByPageReq import GetItemsByPageReq
# from library.common.Rsp.AccountRsp import SearchAccountsRsp
# from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
# from library.common.Rsp.SingleRsp import ErrorRsp
# from library.auth import token_required
# from library.repository import EmployeeRep, CustomerRep, AccountRep
# import smtplib
# from email.message import EmailMessage
#
from library.common.Req.AccountReq import *


@app.route('/abc', methods=['POST','GET'])
def DeleteAccount():
    return "Test"

@app.route('/admin/account-management/create-account', methods=['POST'])
def CreateAccount():
    req = CreateAccountReq(request.json)
    result = AccountSvc.CreateAccount(req)
    return result

#
#
# @app.route('/admin/account-management/get-accounts', methods=['POST'])
# @token_required
# def GetAccounts():
#     req = GetItemsByPageReq(request.json)
#     result = AccountSvc.GetAccountsByPage(req)
#     res = GetItemsByPageRsp(hasNext=result['hasNext'], hasPrev=result['hasPrev'],
#                             items=result['accounts']).serialize()
#     return jsonify(res)
#
#
@app.route('/admin/account-management/delete-account', methods=['POST'])
@owner_required
def deleteAccount(account):
    res = AccountSvc.deleteAccount(account)
    return jsonify(res)
#
#
# @app.route('/admin/account-management/get-account', methods=['POST'])
# def SearchAccounts():
#     req = SearchAccountsReq(request.json)
#     info_accounts = AccountSvc.SearchAccounts(req)
#     res = SearchAccountsRsp(info_accounts).serialize()
#     return jsonify(res)
#
#
@app.route('/admin/account-management/login', methods=['POST'])
def LoginAccount():
    try:
        req = LoginReq(request.json)
        result = AccountSvc.login(req)
        res = LoginRsp(result).serialize()
        return jsonify(res)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8'), 401


@app.route('/admin/account-management/session-info', methods=['POST', 'GET'])
def GetSessionInfo():
    auth_headers = request.headers.get('Authorization', '').split()
    token = auth_headers[1]

    try:
        result = AccountSvc.sessionInfo(token)
        res = SessionInfoRsp(result).serialize()
        return jsonify(res)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8'), 401


# @app.route('/send-reset-password-email-customer', methods=['POST'])
# def SendResetPasswordEmailCustomer():
#     req = SendResetPasswordEmailReq(request.json)
#     result = AccountSvc.SendResetPasswordEmailCustomer(req)
#     return jsonify(result)
#
#
# @app.route('/send-reset-password-email-employee', methods=['POST'])
# def SendResetPasswordEmailEmployee():
#     req = SendResetPasswordEmailReq(request.json)
#     result = AccountSvc.SendResetPasswordEmailEmployee(req)
#     return result
#
#
# @app.route('/reset-password', methods=['POST'])
# def ResetPassword():
#     req = ResetPasswordReq(request.json)
#     result = AccountSvc.ResetPassword(req)
#     return jsonify(result)
#
#
@app.route('/admin/account-management/change-password', methods=['POST'])
@user_required
def changePassword(account):
    try:
        req = ChangePasswordReq(request.json)
        req.id=account["id"]
        print(req.__dict__)
        result = AccountSvc.changePassword(req)
        return jsonify(result)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8'), 401
#
#
# @app.route('/create-customer-account', methods=['POST'])
# def CreateCustomerAccount():
#     try:
#         req = CreateCustomerAccountReq(request.json)
#         result = AccountSvc.CreateCustomerAccount(req)
#         return jsonify(result)
#     except ErrorRsp as e:
#         return json.dumps(e.__dict__, ensure_ascii=False).encode('utf-8'), 401
#
#
# @app.route('/create-employee-account', methods=['POST'])
# def CreateEmployeeAccount():
#     try:
#         req = CreateEmployeeAccountReq(request.json)
#         result = AccountSvc.CreateEmployeeAccount(req)
#         return jsonify(result)
#     except ErrorRsp as e:
#         return json.dumps(e.__dict__, ensure_ascii=False).encode('utf-8'), 401
