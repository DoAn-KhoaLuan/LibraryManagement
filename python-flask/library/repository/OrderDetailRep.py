# from sqlalchemy import or_
#
# from library import db
# from library.common.Req.OrderDetailReq import CreateOrderDetailReq
# from library.repository import models
# from flask import jsonify, json
# from library.common.util import ConvertModelListToDictList
# from library.common.Req import GetItemsByPageReq
# from datetime import datetime
#
#
# def GetOrderDetailsByPage(req: GetItemsByPageReq):
#     order_detail_pagination = models.Orderdetails.query.filter(models.Orderdetails.delete_at == None).paginate(per_page=req.per_page, page=req.page)
#     hasNext = order_detail_pagination.hasNext
#     hasPrev = order_detail_pagination.hasPrev
#     order_details = ConvertModelListToDictList(order_detail_pagination.items)
#     return hasNext, hasPrev, order_details
#
#
# def CreateOrderDetail(req: CreateOrderDetailReq):
#     create_order_detail = models.Orderdetails(order_id=req.order_id,
#                                               book_id=req.book_id,
#                                               retail_price=req.retail_price,
#                                               quantity=req.quantity,
#                                               discount=req.discount,
#                                               total=req.total,
#                                               note=req.note,
#                                               delete_at=req.delete_at)
#
#     db.session.add(create_order_detail)
#     db.session.commit()
#     return create_order_detail.serialize()
