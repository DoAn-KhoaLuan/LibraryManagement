from library import app
from library.BLL import CustomerSvc
from library.Common.Req.CustomerReq import CreateCustomerReq, UpdateCustomerReq, DeleteCustomerReq, SearchCustomersReq
from library.Common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.Common.Rsp.CustomerRsp import SearchCustomersRsp
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


@app.route('/admin/customer-management/search-customers', methods=['POST', 'GET'])
def SearchCustomers():
    req = SearchCustomersReq(request.json)
    result = CustomerSvc.SearchCustomers(req)
    res = SearchCustomersRsp(result)
    return jsonify(res)


