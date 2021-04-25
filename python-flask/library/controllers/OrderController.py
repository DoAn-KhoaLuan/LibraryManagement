from library import app
from library.BLL import OrderSvc
from library.DAL import models
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq, SearchItemsReq
from library.common.Req.OrderReq import CreateOrderReq, UpdateOrderReq, DeleteOrderReq, SearchOrdersReq
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response
import json

from library.common.Rsp.OrderRsp import SearchOrdersRsp
from library.common.Rsp.SingleRsp import ErrorRsp
from library.common.util import ConvertModelListToDictList


@app.route("/admin/order-management/get-orders", methods=['POST', 'GET'])
def GetOrders():
    req = GetItemsByPageReq(request.json)
    result = OrderSvc.GetOrdersByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['orders']).serialize()
    return jsonify(res)


@app.route("/admin/order-management/create-order", methods=['POST', 'GET'])
def CreateOrder():
    try:
        req = CreateOrderReq(request.json)
        result = OrderSvc.CreateOrder(req)

        return jsonify(result)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8')

@app.route('/admin/order-management/create-order-by-momo', methods=['GET', 'POST'])
def RedirectMomoPage():
    req = CreateOrderReq(request.json)
    res = OrderSvc.CreateOrderByMomo(req)
    if res['errorCode'] == 0:
        result = OrderSvc.CreateOrder(req)
    return jsonify(res)

@app.route("/admin/order-management/update-order", methods=['POST', 'GET'])
def UpdateOrder():
    req = UpdateOrderReq(request.json)
    result = OrderSvc.UpdateOrder(req)
    return jsonify(result)


@app.route("/admin/order-management/delete-order", methods=['POST', 'GET'])
def DeleteOrder():
    req = DeleteOrderReq(request.json)
    result = OrderSvc.DeleteOrder(req)

    return jsonify(result)


@app.route("/admin/order-management/search-orders", methods=['POST', 'GET'])
def SearchOrders():
    req = SearchItemsReq(request.json)
    if (req.order_id):
        orders = models.Orders.query.filter(models.Orders.order_id == req.order_id)
        return jsonify(ConvertModelListToDictList(orders))

    orders = models.Orders.query.all()
    if req.type != None:
        orders = [order for order in orders if order.type == req.type]

    if req.customer_phone != None:
        orders = [order for order in orders if order.customer != None and order.customer.phone == (req.customer_phone)]

    orders = [order for order in orders if order.delete_at == None]
    orders = ConvertModelListToDictList(orders)
    return jsonify(orders)

@app.route("/admin/order-management/test-create-order-momo", methods=['POST', 'GET'])
def TestCreateOrder():
    return jsonify({'test': 111})
