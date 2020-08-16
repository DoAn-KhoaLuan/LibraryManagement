from library import app
from library.BLL import CustomerSvc
from library.Common.Req.CustomerReq import CreateCustomerReq, UpdateCustomerReq, DeleteCustomerReq, \
    SearchCustomerByIdReq, SearchCustomerByIdentityIdReq, SearchCustomerByAccountIdReq, SearchCustomerByPhoneReq
from library.Common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.Common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response
import json

from library.Common.Rsp.SingleRsp import ErrorRsp


@app.route('/admin/customer-management/get-customers', methods=['POST', 'GET'])
def GetCustomers():
    req = GetItemsByPageReq(request.json)
    result = CustomerSvc.GetCustomersByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['customers']).serialize()
    return jsonify(res)


@app.route('/admin/customer-management/create-customer', methods=['POST', 'GET'])
def CreateCustomer():
    req = CreateCustomerReq(request.json)
    result = CustomerSvc.CreateCustomer(req)
    return jsonify(result)


@app.route('/admin/customer-management/update-customer', methods=['POST', 'GET'])
def UpdateCustomer():
    req = UpdateCustomerReq(request.json)
    result = CustomerSvc.UpdateCustomer(req)
    return jsonify(result)


@app.route('/admin/customer-management/delete-customer', methods=['POST', 'GET'])
def DeleteCustomer():
    req = DeleteCustomerReq(request.json)
    result = CustomerSvc.DeleteCustomer(req)
    return jsonify(result)


@app.route('/admin/customer-management/search-customer-by-id', methods=['POST', 'GET'])
def SearchCustomerById():
    req = SearchCustomerByIdReq(request.json)
    result = CustomerSvc.SearchCustomerById(req)
    return jsonify(result)


@app.route('/admin/customer-management/search-customer-by-identity-id', methods=['POST', 'GET'])
def SearchCustomerByIdentityId():
    req = SearchCustomerByIdentityIdReq(request.json)
    result = CustomerSvc.SearchCustomerByIdentityId(req)
    return jsonify(result)


@app.route('/admin/customer-management/search-customer-by-account-id', methods=['POST', 'GET'])
def SearchCustomerByAccountId():
    req = SearchCustomerByAccountIdReq(request.json)
    result = CustomerSvc.SearchCustomerByAccountId(req)
    return jsonify(result)


@app.route('/admin/customer-management/search-customer-by-phone', methods=['POST', 'GET'])
def SearchCustomerByPhone():
    req = SearchCustomerByPhoneReq(request.json)
    result = CustomerSvc.SearchCustomerByPhone(req)
    return jsonify(result)
