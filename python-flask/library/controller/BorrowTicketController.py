# from library import app
# from flask import jsonify, request, make_response
# import json
#
# from library.service import BorrowTicketSvc
# from library.common.Req.BorrowTicketReq import CreateBorrowTicketReq, UpdateBorrowTicketReq, DeleteBorrowTicketReq, \
#     SearchBorrowTicketReq, FinishBorrowTicketReq, SendEmailForLateBorrowTicketReq
# from library.common.Req.GetItemsByPageReq import GetItemsByPageReq
# from library.common.Rsp.BorrowTicketRsp import SearchBorrowTicketRsp
# from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
# from library.common.Rsp.SingleRsp import ErrorRsp
#
#
# @app.route('/admin/borrow-ticket-management/get-borrow-tickets', methods=['POST', 'GET'])
# def GetBorrowTickets():
#     req = GetItemsByPageReq(request.json)
#     result = BorrowTicketSvc.GetBorrowTicketsByPage(req)
#     res = GetItemsByPageRsp(hasNext=result['hasNext'], hasPrev=result['hasPrev'],
#                             items=result['borrow_tickets']).serialize()
#     return jsonify(res)
#
#
# @app.route('/admin/borrow-ticket-management/create-borrow-ticket', methods=['POST', 'GET'])
# def CreateBorrowTicket():
#     req = CreateBorrowTicketReq(request.json)
#     try:
#         result = BorrowTicketSvc.CreateBorrowTicket(req)
#         return jsonify(result)
#     except ErrorRsp as e:
#         return json.dumps(e.__dict__, ensure_ascii=False).encode('utf-8'), 401
#
#
# @app.route('/admin/borrow-ticket-management/update-borrow-ticket', methods=['POST', 'GET'])
# def UpdateBorrowTicket():
#     req = UpdateBorrowTicketReq(request.json)
#     result = BorrowTicketSvc.UpdateBorrowTicket(req)
#     return jsonify(result)
#
#
# @app.route('/admin/borrow-ticket-management/finish-borrow-ticket', methods=['POST', 'GET'])
# def FinishBorrowTicket():
#     req = FinishBorrowTicketReq(request.json)
#     result = BorrowTicketSvc.FinishBorrowTicket(req)
#     return jsonify(result)
#
#
# @app.route('/admin/borrow-ticket-management/delete-borrow-ticket', methods=['POST', 'GET'])
# def DeleteBorrowTicket():
#     req = DeleteBorrowTicketReq(request.json)
#     result = BorrowTicketSvc.DeleteBorrowTicket(req)
#     return jsonify(result)
#
#
# @app.route('/admin/borrow-ticket-management/get-borrow-ticket', methods=['POST', 'GET'])
# def SearchBorrowTicket():
#     req = SearchBorrowTicketReq(request.json)
#     result = BorrowTicketSvc.SearchBorrowTicket(req)
#     res = SearchBorrowTicketRsp(result).serialize()
#     return jsonify(res)
#
# @app.route('/admin/borrow-ticket-management/send-email-for-late-borrow-ticket', methods=['POST', 'GET'])
# def SendEmailForLateBorrowTicket():
#     req = SendEmailForLateBorrowTicketReq(request.json)
#     result = BorrowTicketSvc.SendMessageForLate(req)
#     return jsonify(result)
