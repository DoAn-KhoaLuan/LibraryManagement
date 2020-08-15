from library import db
from library.Common.Req import GetItemsByPageReq
from library.Common.Req.OrderReq import CreateOrderReq, UpdateOrderReq, DeleteOrderReq, SearchOrderByOrderIdReq, \
    SearchOrderByCustomerIdReq, SearchOrderByEmployeeIdReq, SearchOrderByOrderDateReq
from library.Common.Rsp.OrderRsp import SearchOrderByCustomerIdEmployeeIdRsp, SearchOrderByOrderDateRsp
from library.Common.util import ConvertModelListToDictList
from library.DAL import models
from flask import jsonify, json

from datetime import datetime


def GetOrdersbyPage(req: GetItemsByPageReq):
    orders_pagination = models.Orders.query.paginate(per_page=req.per_page, page=req.page)
    has_next = orders_pagination.has_next
    has_prev = orders_pagination.has_prev
    employees = ConvertModelListToDictList(orders_pagination.items)
    return has_next, has_prev, employees


def CreateOrder(req: CreateOrderReq):
    create_order = models.Orders(customer_id=req.customer_id,
                                 employee_id=req.employee_id,
                                 order_date=req.order_date,
                                 type=req.type,
                                 total=req.total,
                                 note=req.note,
                                 delete_at=req.delete_at)
    db.session.add(create_order)
    db.session.commit()
    return create_order.serialize()


def UpdateOrder(req: UpdateOrderReq):
    update_order = models.Orders.query.get(req.order_id)
    update_order.customer_id = req.customer_id
    update_order.employee_id = req.employee_id
    update_order.order_date = req.order_date
    update_order.type = req.type
    update_order.total = req.total
    update_order.note = req.note
    update_order.delete_at = req.delete_at
    db.session.commit()
    return update_order.serialize()


def DeleteOrder(req: DeleteOrderReq):
    delete_order = models.Orders.query.get(req.order_id)
    delete_order.delete_at = datetime.now()
    db.session.add(delete_order)
    db.session.commit()

    return delete_order.serialize()


def SearchOrderByOrderId(req: SearchOrderByOrderIdReq):
    search_order = models.Orders.query.get(req.order_id)
    return search_order.serialize()


def SearchOrderByCustomerId(req: SearchOrderByCustomerIdReq):
    search_order = models.Orders.query.filter(models.Orders.customer_id.contains(req.customer_id)).all()
    orders = ConvertModelListToDictList(search_order)
    res = SearchOrderByCustomerIdEmployeeIdRsp(orders).serialize()
    return res


def SearchOrderByEmployeeId(req: SearchOrderByEmployeeIdReq):
    search_order = models.Orders.query.filter(models.Orders.employee_id.contains(req.employee_id)).all()
    orders = ConvertModelListToDictList(search_order)
    res = SearchOrderByCustomerIdEmployeeIdRsp(orders).serialize()
    return res


def SearchOrderByOrderDate(req: SearchOrderByOrderDateReq):
    search_order = models.Orders.query.filter(models.Orders.order_date.contains(req.order_date))
    orders = ConvertModelListToDictList(search_order)
    res = SearchOrderByOrderDateRsp(orders).serialize()
    return res
