from library import app
from library.BLL import EmployeeSvc
from library.common.Req.EmployeeReq import CreateEmployeeReq, UpdateEmployeeReq, DeleteEmployeeReq, SearchEmployeesReq
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.common.Rsp.EmployeeRsp import SearchEmployeeRsp
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response
import json

from library.common.Rsp.SingleRsp import ErrorRsp


@app.route('/admin/employee-management/get-employees', methods=['POST', 'GET'])
def GetEmployees():
    req = GetItemsByPageReq(request.json)
    result = EmployeeSvc.GetEmployeesByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['employees']).serialize()
    return jsonify(res)


@app.route('/admin/employee-management/create-employee', methods=['POST'])
def CreateEmployee():
    req = CreateEmployeeReq(request.json)
    result = EmployeeSvc.CreateEmployee(req)
    return jsonify(result)


@app.route('/admin/employee-management/update-employee', methods=['POST'])
def UpdateEmployee():
    req = UpdateEmployeeReq(request.json)
    result = EmployeeSvc.UpdateEmployee(req)
    return jsonify(result)


@app.route('/admin/employee-management/delete-employee', methods=['POST'])
def DeleteEmployee():
    req = DeleteEmployeeReq(request.json)
    result = EmployeeSvc.DeleteEmployee(req)
    return jsonify(result)


@app.route('/admin/employee-management/search-employees', methods=['POST'])
def SearchEmployees():
    req = SearchEmployeesReq(request.json)
    result = EmployeeSvc.SearchEmployee(req)
    res = SearchEmployeeRsp(result).serialize()
    return jsonify(result)

