from library import app
from library.auth import owner_required
from library.common.Req.PageReq import SearchItemsReq
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
        req = CreateOrderReq(request.json)
        req.sellerAccountId = account["id"]
        req.shopId = account["shop"]["id"]
        result = OrderSvc.createOrder(req)

        return jsonify(result)
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
