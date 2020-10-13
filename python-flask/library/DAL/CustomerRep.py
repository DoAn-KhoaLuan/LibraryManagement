from sqlalchemy import or_

from library import db
from library.Common.Req import GetItemsByPageReq
from library.Common.Req.AccountReq import SendResetPasswordEmailReq
from library.Common.Req.CustomerReq import CreateCustomerReq, UpdateCustomerReq, DeleteCustomerReq
from library.Common.Req.CustomerReq import CreateCustomerReq, UpdateCustomerReq, DeleteCustomerReq, SearchCustomersReq
from library.Common.Rsp.CustomerRsp import SearchCustomersRsp
from library.Common.util import ConvertModelListToDictList
from library.DAL import models
from flask import jsonify, json
from library.DAL.models import Accounts
from datetime import datetime
from library.Common.util import ConvertModelListToDictList
import pytz


def GetCustomersByPage(req: GetItemsByPageReq):
    customers_pagination = models.Customers.query.filter(models.Customers.delete_at == None).paginate(per_page=req.per_page, page=req.page)
    has_next = customers_pagination.has_next
    has_prev = customers_pagination.has_prev
    customers = ConvertModelListToDictList(customers_pagination.items)
    return has_next, has_prev, customers


def CreatCustomer(req: CreateCustomerReq):
    create_customer = models.Customers(identity_id=req.identity_id,
                                       account_id=req.account_id,
                                       last_name=req.last_name,
                                       first_name=req.first_name,
                                       phone=req.phone,
                                       student_code=req.student_code,
                                       birth_date=req.birth_date,
                                       address=req.address,
                                       gender=req.gender,
                                       email=req.email,
                                       note=req.note,
                                       delete_at=req.delete_at)
    db.session.add(create_customer)
    db.session.commit()
    return create_customer.serialize()


def UpdateCustomer(req: UpdateCustomerReq):
    update_customer = models.Customers.query.get(req.customer_id)
    update_customer.identity_id = req.identity_id
    update_customer.account_id = req.account_id
    update_customer.last_name = req.last_name
    update_customer.first_name = req.first_name
    update_customer.phone = req.phone
    update_customer.student_code = req.student_code
    update_customer.birth_date = req.birth_date
    update_customer.address = req.address
    update_customer.gender = req.gender
    update_customer.email = req.email
    update_customer.note = req.note
    update_customer.delete_at = req.delete_at
    db.session.commit()
    return update_customer.serialize()


def DeleteCustomer(req: DeleteCustomerReq):
    delete_customer = models.Customers.query.get(req.customer_id)
    delete_customer.delete_at = datetime.now(tz=pytz.timezone("Asia/Ho_Chi_Minh"))
    db.session.add(delete_customer)
    db.session.commit()
    return delete_customer.serialize()


def SearchCustomers(req: SearchCustomersReq):
    search_customer = models.Customers.query.filter(or_(models.Customers.customer_id == req.customer_id,
                                                        models.Customers.account_id == req.account_id,
                                                        models.Customers.identity_id == req.identity_id,
                                                        models.Customers.phone == req.phone)).all()
    customer = models.Customers.query.get(models.Customers.customer_id == 1).all()
    for i in customer:
        if i:
            print(customer.orders)
    customers = ConvertModelListToDictList(search_customer)
    return customers


