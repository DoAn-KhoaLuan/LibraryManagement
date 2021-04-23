from flask import request, jsonify

from library import app
from library.BLL import SupplierSvc
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.common.Req.SupplierReq import CreateSupplierReq, UpdateSupplierReq, DeleteSupplierReq, SearchSuppliersReq
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from library.common.Rsp.SupplierRsp import SearchSuppliersRsp


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
    req = UpdateSupplierReq(request.json)
    result = SupplierSvc.UpdateSupplier(req)
    return jsonify(result)


@app.route('/admin/supplier-management/search-suppliers', methods=['POST'])
def SearchSuppliers():
    req = SearchSuppliersReq(request.json)
    result = SupplierSvc.SearchSuppliers(req)
    res = SearchSuppliersRsp(result).serialize()
    return jsonify(res['suppliers'])


@app.route('/admin/supplier-management/delete-supplier', methods=['POST'])
def DeleteSupplier():
    req = DeleteSupplierReq(request.json)
    result = SupplierSvc.DeleteSupplier(req)
    return jsonify(result)
