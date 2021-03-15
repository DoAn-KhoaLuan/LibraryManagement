# import json
# from datetime import datetime, timedelta
# from functools import wraps
#
# import jwt
# from flask import request, jsonify
#
import json
from datetime import datetime
import requests
from flask import request, jsonify
from pymysql import Date

from library import app
from library.common.Rsp.AccountRsp import SessionInfoRsp
from library.common.Rsp.SingleRsp import ErrorRsp
from library.repository import *
from library.repository import CategoryRep, LocationRep
from library.service import AccountSvc, CategorySvc
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
from miration.models import *


@app.route('/abc', methods=['POST'])
def DeleteAccount():
    return "Test"

@app.route('/admin/account-management/create-account', methods=['POST'])
def CreateAccount():
    req = CreateAccountReq(request.json)
    result = AccountSvc.CreateAccount(req)
    return result
# @app.route('/admin/account-management/create-account', methods=['POST'])
# def CreateAccount() -> CreateAccountReq:
#     req = CreateAccountReq(request.json)
#     result = AccountSvc.CreateAccount(req)
#     return result
#
#
# @app.route('/admin/account-management/get-accounts', methods=['POST'])
# @token_required
# def GetAccounts():
#     req = GetItemsByPageReq(request.json)
#     result = AccountSvc.GetAccountsByPage(req)
#     res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
#                             items=result['accounts']).serialize()
#     return jsonify(res)
#
#
# @app.route('/admin/account-management/delete-account', methods=['POST'])
# def DeleteAccount():
#     req = DeleteAccountReq(request.json)
#     res = AccountSvc.DeleteAccount(req)
#     return jsonify(res.serialize())
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
        result = AccountSvc.Login(req)
        res = LoginRsp(result).serialize()
        return jsonify(res)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8'), 401


@app.route('/admin/account-management/login', methods=['POST', 'GET'])
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
# @app.route('/change-password', methods=['POST'])
# def ChangePassword():
#     try:
#         req = ChangePasswordReq(request.json)
#         result = AccountSvc.ChangePassword(req)
#         return jsonify(result)
#     except ErrorRsp as e:
#         return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8'), 401
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
