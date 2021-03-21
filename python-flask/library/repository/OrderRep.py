from sqlalchemy import or_

from library import db
from library.common.Req import GetItemsByPageReq
from library.common.Req.OrderReq import CreateOrderReq, UpdateOrderReq, DeleteOrderReq, SearchOrdersReq
from library.common.Req.PageReq import DeleteItemReq
from library.common.Rsp.OrderRsp import SearchOrdersRsp
from library.common.Rsp.SingleRsp import ErrorRsp
from library.common.util import ConvertModelListToDictList
from flask import jsonify, json

from datetime import datetime


def GetOrdersbyPage(req: GetItemsByPageReq):
    orderPagination = models.Order.query.filter(models.Order.deleteAt == None,
                                                models.Order.shopId == req.shopId
                                                )\
        .paginate(per_page=req.perPage, page = req.page)
    hasNext = orderPagination.has_next
    hasPrev = orderPagination.has_prev
    orders = ConvertModelListToDictList(orderPagination.items)
    return hasNext, hasPrev, orders
#
from library.miration import models


def createOrder(order: CreateOrderReq):
    sellerAccount = models.Account.query.get(order.sellerAccountId)
    buyerAccount = models.Account.query.get(order.buyerAccountId)
    createOrder = models.Order(sellerAccount=sellerAccount,
                               buyerAccount=buyerAccount,
                               shopId=order.shopId,
                                createAt=datetime.now(),
                                type=order.type,
                                note=order.note)

    db.session.add(createOrder)
    db.session.commit()
    total = 0.0
    quantity = 0
    for orderDetail in order.orderDetailList:
        orderProduct = models.Product.query.get(orderDetail['productId'])
        orderProduct.amount -= orderDetail['quantity']
        if orderProduct.amount < 0:
            raise ErrorRsp(code=400, message='Số lượng sản phẩm tồn kho đã hết.')
        detailTotal = (1 - orderDetail['discount']) * (orderProduct.retailPrice * orderDetail['quantity'])
        newOrderDetail = models.OrderDetail(orderId=createOrder.serialize()['id'],
                                            productId=orderDetail['productId'],
                                            retailPrice=orderProduct.retailPrice,
                                            discount= orderDetail['discount'],
                                            quantity= orderDetail['quantity'],
                                            total=detailTotal
                                            )
        total += detailTotal
        quantity += orderDetail['quantity']
        createOrder.orderDetails.append(newOrderDetail)
    createOrder.total = total
    createOrder.quantity = quantity
    db.session.commit()
    return createOrder.serialize()


# def UpdateOrder(req: UpdateOrderReq):
#     update_order = models.Orders.query.get(req.order_id)
#     update_order.customer_id = req.customer_id
#     update_order.employee_id = req.employee_id
#     update_order.order_date = req.order_date
#     update_order.type = req.type
#     update_order.total = req.total
#     update_order.note = req.note
#     update_order.delete_at = req.delete_at
#     db.session.commit()
#     retuer.serialize()
#
#
def deleteOrder(req: DeleteItemReq):
    deleteOrder = models.Order.query.get(req.id)
    deleteOrder.deleteAt = datetime.now()
    db.session.add(deleteOrder)
    db.session.commit()

    return deleteOrder.serialize()
#
#
# def SearchOrders(req: SearchOrdersReq):
#     search_orders = models.Orders.query.filter(or_(models.Orders.customer_id == req.customer_id,
#                                                   models.Orders.order_id == req.order_id,
#                                                   models.Orders.employee_id == req.employee_id,
#                                                   models.Orders.order_date == req.order_date)).all()
#     orders = ConvertModelListToDictList(search_orders)
#     return orders
