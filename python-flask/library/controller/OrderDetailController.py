# from library import app
# from flask import jsonify, request, make_response
# import json
#
# from library.service import OrderDetailSvc
# from library.common.Req.GetItemsByPageReq import GetItemsByPageReq
# from library.common.Req.OrderDetailReq import CreateOrderDetailReq
# from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
# from library.common.Rsp.SingleRsp import ErrorRsp
#
#
# @app.route('/admin/order-detail-management/get-order-details', methods=['POST', 'GET'])
# def GetOrderDetails():
#     req = GetItemsByPageReq(request.json)
#     result = OrderDetailSvc.GeOrderDetailsByPage(req)
#     res = GetItemsByPageRsp(hasPrev=result['hasPrev'], hasNext=result['hasNext'],
#                             items=result['order_details']).serialize()
#     return jsonify(res)
#
#
# @app.route('/admin/order-detail-management/create-order-detail', methods=['POST', 'GET'])
# def CreateOrderDetail():
#     req = CreateOrderDetailReq(request.json)
#     result = OrderDetailSvc.CreateOrderDetail(req)
#     return jsonify(result)
