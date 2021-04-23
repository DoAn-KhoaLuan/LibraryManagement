from datetime import datetime

from library import app, db
from library.auth import owner_required
from library.common.Req.PageReq import SearchItemsReq
from library.miration import models
from library.service import OrderSvc
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.common.Req.OrderReq import CreateOrderReq, UpdateOrderReq, DeleteOrderReq, SearchOrdersReq
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response
import json
#
from library.common.Rsp.OrderRsp import SearchOrdersRsp
from library.common.Rsp.SingleRsp import ErrorRsp
#
#
@app.route("/admin/order-management/get-orders-by-shop", methods=['POST', 'GET'])
@owner_required
def GetOrders(account):
    req = GetItemsByPageReq(request.json)
    req.shopId = account["shop"]["id"]
    result = OrderSvc.GetOrdersByPage(req)
    res = GetItemsByPageRsp(hasNext=result['hasNext'], hasPrev=result['hasPrev'],
                            items=result['orders']).serialize()
    return jsonify(res)


@app.route("/admin/order-management/create-order", methods=['POST', 'GET'])
@owner_required
def createOrder(account):
    try:
        order = CreateOrderReq(request.json)
        order.sellerAccountId = account["id"]
        order.shopId = account["shop"]["id"]

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
                                                discount=orderDetail['discount'],
                                                quantity=orderDetail['quantity'],
                                                total=detailTotal
                                                )
            total += detailTotal
            quantity += orderDetail['quantity']
            createOrder.orderDetails.append(newOrderDetail)
        createOrder.total = total
        createOrder.quantity = quantity
        db.session.commit()

        return jsonify(createOrder.serialize())
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8')
#
# @app.route('/admin/order-management/create-order-by-momo', methods=['GET', 'POST'])
# def RedirectMomoPage():
#     req = CreateOrderReq(request.json)
#     res = OrderSvc.CreateOrderByMomo(req)
#     if res['errorCode'] == 0:
#         result = OrderSvc.CreateOrder(req)
#     return jsonify(res)


@app.route("/admin/order-management/update-order", methods=['POST', 'GET'])
def UpdateOrder():
    req = UpdateOrderReq(request.json)
    result = OrderSvc.UpdateOrder(req)
    return jsonify(result)


@app.route("/admin/order-management/delete-order", methods=['POST', 'GET'])
@owner_required
def deleteOrder(account):
    req = DeleteOrderReq(request.json)
    result = OrderSvc.deleteOrder(req)

    return jsonify(result)
#
#
@app.route("/admin/order-management/search-orders-by-shop", methods=['POST', 'GET'])
@owner_required
def searchOrdersByShop(account):
    req = SearchItemsReq(request.json)
    req.shopId = account["shop"]["id"]
    orders = OrderSvc.searchOrdersByShop(req)
    res = SearchOrdersRsp(orders).serialize()
    return jsonify(res)
#
# @app.route("/admin/order-management/test-create-order-momo", methods=['POST', 'GET'])
# def TestCreateOrder():
#     return jsonify({'test': 111})
