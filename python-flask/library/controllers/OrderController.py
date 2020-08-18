from library import app
from library.BLL import OrderSvc
from library.Common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.Common.Req.OrderReq import CreateOrderReq, UpdateOrderReq, DeleteOrderReq, SearchOrdersReq
from library.Common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response
import json

from library.Common.Rsp.SingleRsp import ErrorRsp


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
    req = SearchOrdersReq(request.json)
    result = OrderSvc.SearchOrders(req)

    return jsonify(result)


