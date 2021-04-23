# from library import app
from library import app
from library.common.util import ConvertModelListToDictList
from library.miration import models
from library.service import CustomerSvc
from library.common.Req.CustomerReq import CreateCustomerReq, UpdateCustomerReq, DeleteCustomerReq, SearchCustomersReq
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.common.Rsp.CustomerRsp import SearchCustomersRsp
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response
import json

from library.common.Rsp.SingleRsp import ErrorRsp
#
#
@app.route('/admin/customer-management/get-customers', methods=['POST', 'GET'])
def GetCustomers():
    req = GetItemsByPageReq(request.json)
    customers_pagination = models.Customer.query.filter(models.Customers.delete_at == None).paginate(
        per_page=req.per_page, page=req.page)
    hasNext = customers_pagination.hasNext
    hasPrev = customers_pagination.hasPrev
    customers = ConvertModelListToDictList(customers_pagination.items)
    res = GetItemsByPageRsp(hasNext=hasNext, hasPrev=hasPrev,
                            items=customers).serialize()
    return jsonify(res.serialize())
#
#
# @app.route('/admin/customer-management/create-customer', methods=['POST', 'GET'])
# def CreateCustomer():
#     req = CreateCustomerReq(request.json)
#     result = CustomerSvc.CreateCustomer(req)
#     return jsonify(result)
#
#
# @app.route('/admin/customer-management/update-customer', methods=['POST', 'GET'])
# def UpdateCustomer():
#     req = UpdateCustomerReq(request.json)
#     result = CustomerSvc.UpdateCustomer(req)
#     return jsonify(result)
#
#
# @app.route('/admin/customer-management/delete-customer', methods=['POST', 'GET'])
# def DeleteCustomer():
#     req = DeleteCustomerReq(request.json)
#     result = CustomerSvc.DeleteCustomer(req)
#     return jsonify(result)
#
#
# @app.route('/admin/customer-management/search-customers', methods=['POST', 'GET'])
# def SearchCustomers():
#     req = SearchCustomersReq(request.json)
#     result = CustomerSvc.SearchCustomers(req)
#     res = SearchCustomersRsp(result)
#     return jsonify(result)
#
#
