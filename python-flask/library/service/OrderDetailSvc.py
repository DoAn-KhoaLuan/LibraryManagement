# from library.repository import OrderDetailRep
#
#
# def GeOrderDetailsByPage(req):
#     hasNext, hasPrev, order_details = OrderDetailRep.GetOrderDetailsByPage(req)
#     result = {
#         "hasNext": hasNext,
#         "hasPrev": hasPrev,
#         "order_details": order_details
#     }
#     return result
#
#
# def CreateOrderDetail(req):
#     create_order_detail = OrderDetailRep.CreateOrderDetail(req)
#     return create_order_detail
