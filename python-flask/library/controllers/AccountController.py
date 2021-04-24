import json
from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import request, jsonify

from library import app, smtp, db
from library.BLL import AccountSvc
from library.common.Req.AccountReq import CreateAccountReq, DeleteAccountReq, LoginReq, LoginRsp, SearchAccountsReq, \
    SendResetPasswordEmailReq, ResetPasswordReq, ChangePasswordReq, CreateCustomerAccountReq, CreateEmployeeAccountReq
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.common.Rsp.AccountRsp import SearchAccountsRsp
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from library.common.Rsp.SingleRsp import ErrorRsp
from library.DAL import EmployeeRep, CustomerRep, AccountRep, models, LocationRep
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


@app.route('/admin/account-management/get-account', methods=['POST'])
def SearchAccounts():
    req = SearchAccountsReq(request.json)
    info_accounts = AccountSvc.SearchAccounts(req)
    res = SearchAccountsRsp(info_accounts).serialize()
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
    return jsonify(result)


@app.route('/send-reset-password-email-employee', methods=['POST'])
def SendResetPasswordEmailEmployee():
    req = SendResetPasswordEmailReq(request.json)
    result = AccountSvc.SendResetPasswordEmailEmployee(req)
    return result


@app.route('/reset-password', methods=['POST'])
def ResetPassword():
    req = ResetPasswordReq(request.json)
    result = AccountSvc.ResetPassword(req)
    return jsonify(result)


@app.route('/change-password', methods=['POST'])
def ChangePassword():
    try:
        req = ChangePasswordReq(request.json)
        result = AccountSvc.ChangePassword(req)
        return jsonify(result)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8'), 401


@app.route('/create-customer-account', methods=['POST'])
def CreateCustomerAccount():
    try:
        req = CreateCustomerAccountReq(request.json)
        result = AccountSvc.CreateCustomerAccount(req)
        return jsonify(result)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf-8'), 401


@app.route('/create-employee-account', methods=['POST'])
def CreateEmployeeAccount():
    try:
        req = CreateEmployeeAccountReq(request.json)
        result = AccountSvc.CreateEmployeeAccount(req)
        return jsonify(result)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf-8'), 401

@app.route('/create-role', methods=['POST'])
def CreateRole():
    try:
        req = CreateEmployeeAccountReq(request.json)
        role = models.Roles(role_id=1,role_name= "admin", note="note", delete_at=None)
        role1 = models.Roles(role_id=2,role_name= "admin-manager", note="note", delete_at=None)
        role2 = models.Roles(role_id=3,role_name= "user", note="note", delete_at=None)
        db.session.add(role)
        db.session.add(role1)
        db.session.add(role2)
        db.session.commit()
        return jsonify({})
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf-8'), 401



@app.route('/get-provinces', methods=['POST'])
def getProvinces():
    return jsonify(LocationRep.getProvinces())


@app.route('/get-districts', methods=['POST'])
def getDistricts():
    return jsonify(LocationRep.getDistricts())


@app.route('/get-wards', methods=['POST'])
def getWards():
    return jsonify(LocationRep.getWards())
