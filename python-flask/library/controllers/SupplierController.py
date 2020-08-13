from flask import request, jsonify

from library import app
from library.BLL import SupplierSvc
from library.Common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.Common.Req.SupplierReq import CreateSupplierReq, UpdateSupplierReq, SearchSupplierByIdReq, \
    SearchSupplierByContactNameReq
from library.Common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp


@app.route('/admin/supplier-management/get-suppliers', methods=['GET', 'POST'])
def GetSuplliers():
    req = GetItemsByPageReq(request.json)
    result = SupplierSvc.GetSupplierByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['suppliers']).serialize()
    return jsonify(res)


@app.route('/admin/supplier-management/create-supplier', methods=['POST'])
def CreateSupplier():
    req = CreateSupplierReq(request.json)
    result = SupplierSvc.CreateSupplier(req)
    return jsonify(result)


@app.route('/admin/supplier-management/update-supplier', methods=['POST'])
def UpdateSupplier():
    req =  UpdateSupplierReq(request.json)
    result = SupplierSvc.UpdateSupplier(req)
    return jsonify(result)


@app.route('/admin/supplier-management/search-supplier-by-id', methods=['POST'])
def SearchSupplierById():
    req = SearchSupplierByIdReq(request.json)
    result = SupplierSvc.SearchSupplierById(req)
    return jsonify(result)


@app.route('/admin/supplier-management/search-supplier-by-contact-name', methods=['POST'])
def SearchSupplierByContactName():
    req = SearchSupplierByContactNameReq(request.json)
    result = SupplierSvc.SearchSupplierByContactName(req)
    return jsonify(result)