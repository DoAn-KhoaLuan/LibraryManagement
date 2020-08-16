from datetime import datetime
from time import gmtime, strftime

from sqlalchemy import or_

from library import db
from library.Common.Req import GetItemsByPageReq
from library.Common.Req.EmployeeReq import CreateEmployeeReq, UpdateEmployeeReq, DeleteEmployeeReq, SearchEmployeeReq
from library.Common.Rsp.EmployeeRsp import SearchEmployeeRsp
from library.Common.util import ConvertModelListToDictList
from library.DAL import models
from flask import jsonify, json
from datetime import datetime


def GetEmployeesbyPage(req: GetItemsByPageReq):
    employees_pagination = models.Employees.query.paginate(per_page=req.per_page, page=req.page)
    has_next = employees_pagination.has_next
    has_prev = employees_pagination.has_prev
    employees = ConvertModelListToDictList(employees_pagination.items)
    return has_next, has_prev, employees


def CreateEmployee(req: CreateEmployeeReq):
    create_employee = models.Employees(identity_id=req.identity_id,
                                       account_id=req.account_id,
                                       last_name=req.last_name,
                                       first_name=req.first_name,
                                       phone=req.phone,
                                       birth_date=req.birth_date,
                                       hire_date=req.hire_date,
                                       address=req.address,
                                       gender=req.gender,
                                       image=req.image,
                                       basic_rate=req.basic_rate,
                                       note=req.note,
                                       delete_at=req.delete_at)
    db.session.add(create_employee)
    db.session.commit()
    return create_employee.serialize()


def UpdateEmployee(req: UpdateEmployeeReq):
    update_employee = models.Employees.query.get(req.employee_id)
    update_employee.identity_id = req.identity_id
    update_employee.account_id = req.account_id
    update_employee.last_name = req.last_name
    update_employee.first_name = req.first_name
    update_employee.phone = req.phone
    update_employee.birth_date = req.birth_date
    update_employee.hire_date = req.hire_date
    update_employee.address = req.address
    update_employee.gender = req.gender
    update_employee.image = req.image
    update_employee.basic_rate = req.basic_rate
    update_employee.note = req.note
    update_employee.delete_at = req.delete_at
    db.session.commit()
    return update_employee.serialize()


def DeleteEmployee(req: DeleteEmployeeReq):
    delete_employee = models.Employees.query.get(req.employee_id)
    delete_employee.delete_at = datetime.now()
    db.session.add(delete_employee)
    db.session.commit()

    return delete_employee.serialize()


def SearchEmployees(req: SearchEmployeeReq):
    search_employee = models.Employees.query.filter(or_(models.Employees.first_name == req.keyword,
                                                        models.Employees.last_name == req.keyword,
                                                        models.Employees.identity_id == req.keyword,
                                                        models.Employees.account_id == req.keyword,
                                                        models.Employees.phone == req.keyword,
                                                        models.Employees.employee_id == req.keyword)).all()
    employees = ConvertModelListToDictList(search_employee)
    return employees



