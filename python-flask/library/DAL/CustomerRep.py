from library import db
from library.Common.Req import GetItemsByPageReq
from library.Common.Req.CustomerReq import CreateCustomerReq, UpdateCustomerReq, DeleteCustomerReq, \
    SearchCustomerByIdReq, SearchCustomerByIdentityIdReq, SearchCustomerByAccountIdReq, SearchCustomerByPhoneReq
from library.Common.Rsp.CustomerRsp import SearchCustomerByIdentityIdRsp, SearchCustomerByAccountIdRsp, \
    SearchCustomerByPhoneRsp
from library.Common.util import ConvertModelListToDictList
from library.DAL import models
from flask import jsonify, json
from library.DAL.models import Accounts
from datetime import datetime
from library.Common.util import ConvertModelListToDictList


def GetCustomersByPage(req: GetItemsByPageReq):
    customers_pagination = models.Customers.query.paginate(per_page=req.per_page, page=req.page)
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
    delete_customer.delete_at = datetime.now()
    db.session.add(delete_customer)
    db.session.commit()
    return delete_customer.serialize()


def SearchCustomerById(req: SearchCustomerByIdReq):
    search_customer = models.Customers.query.get(req.customer_id)
    return search_customer.serialize()


def SearchCustomerByIdentityId(req: SearchCustomerByIdentityIdReq):
    search_customer = models.Customers.query.filter(models.Customers.identity_id.contains(req.identity_id)).all()
    customers = ConvertModelListToDictList(search_customer)
    res = SearchCustomerByIdentityIdRsp(customers).serialize()
    return res


def SearchCustomerByAccountId(req: SearchCustomerByAccountIdReq):
    search_customer = models.Customers.query.filter(models.Customers.account_id.contains(req.account_id)).all()
    customers = ConvertModelListToDictList(search_customer)
    res = SearchCustomerByAccountIdRsp(customers).serialize()
    return res


def SearchCustomerByPhone(req: SearchCustomerByPhoneReq):
    search_customer = models.Customers.query.filter(models.Customers.phone.contains(req.phone)).all()
    customers = ConvertModelListToDictList(search_customer)
    res = SearchCustomerByPhoneRsp(customers).serialize()
    return res
