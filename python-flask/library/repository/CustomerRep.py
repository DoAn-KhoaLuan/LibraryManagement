# from sqlalchemy import or_
#
# from library import db
# from library.common.Req import GetItemsByPageReq
# from library.common.Req.AccountReq import SendResetPasswordEmailReq
# from library.common.Req.CustomerReq import CreateCustomerReq, UpdateCustomerReq, DeleteCustomerReq
# from library.common.Req.CustomerReq import CreateCustomerReq, UpdateCustomerReq, DeleteCustomerReq, SearchCustomersReq
# from library.common.Rsp.CustomerRsp import SearchCustomersRsp
# from library.common.util import ConvertModelListToDictList
# from library.repository import models
# from flask import jsonify, json
# from library.repository.models import Accounts
# from datetime import datetime
# from library.common.util import ConvertModelListToDictList
#
#
# def GetCustomersByPage(req: GetItemsByPageReq):
#     customers_pagination = models.Customers.query.filter(models.Customers.delete_at == None).paginate(per_page=req.per_page, page=req.page)
#     hasNext = customers_pagination.hasNext
#     hasPrev = customers_pagination.hasPrev
#     customers = ConvertModelListToDictList(customers_pagination.items)
#     return hasNext, hasPrev, customers
#
#
# def CreatCustomer(req: CreateCustomerReq):
#     create_customer = models.Customers(identity_id=req.identity_id,
#                                        account_id=req.account_id,
#                                        last_name=req.last_name,
#                                        first_name=req.first_name,
#                                        phone=req.phone,
#                                        student_code=req.student_code,
#                                        birth_date=req.birth_date,
#                                        address=req.address,
#                                        gender=req.gender,
#                                        email=req.email,
#                                        note=req.note,
#                                        delete_at=req.delete_at)
#     db.session.add(create_customer)
#     db.session.commit()
#     return create_customer.serialize()
#
#
# def UpdateCustomer(req: UpdateCustomerReq):
#     update_customer = models.Customers.query.get(req.customer_id)
#     update_customer.identity_id = req.identity_id
#     update_customer.account_id = req.account_id
#     update_customer.last_name = req.last_name
#     update_customer.first_name = req.first_name
#     update_customer.phone = req.phone
#     update_customer.student_code = req.student_code
#     update_customer.birth_date = req.birth_date
#     update_customer.address = req.address
#     update_customer.gender = req.gender
#     update_customer.email = req.email
#     update_customer.note = req.note
#     update_customer.delete_at = req.delete_at
#     db.session.commit()
#     return update_customer.serialize()
#
#
# def DeleteCustomer(req: DeleteCustomerReq):
#     delete_customer = models.Customers.query.get(req.customer_id)
#     delete_customer.delete_at = datetime.now()
#     db.session.add(delete_customer)
#     db.session.commit()
#     return delete_customer.serialize()
#
#
# def SearchCustomers(req: SearchCustomersReq):
#     search_customer = models.Customers.query.filter(or_(models.Customers.customer_id == req.customer_id,
#                                                         models.Customers.account_id == req.account_id,
#                                                         models.Customers.identity_id == req.identity_id,
#                                                         models.Customers.phone == req.phone)).all()
#     customers = ConvertModelListToDictList(search_customer)
#     return customers
#
#
