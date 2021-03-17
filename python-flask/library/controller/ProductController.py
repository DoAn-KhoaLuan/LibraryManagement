
from library import app
from library.common.Req.ProductReq import *
from library.service import ProductSvc

from library.common.Rsp.BookRsp import DeleteBookByIdRsp, UpdateBookRsp, SearchBookRsp, CreateProductRsp

from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request

from library.common.Rsp.SingleRsp import ErrorRsp
from library.auth import user_required, owner_required


# from library.controller.UploadImageController import allowed_file


# @app.route('/admin/book-management/get-books', methods=['POST'])
# @token_required
# def GetBooks(auth_info):
#     try:
#         req = GetItemsByPageReq(request.json)
#         result = BookSvc.GetBooksByPage(req)
#         res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
#                                 items=result['books']).serialize()
#         return jsonify(res)
#     except ErrorRsp as e:
#         return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8')
#
#
@app.route('/admin/product-management/create-product', methods=['POST'])
@owner_required
def CreateBook(account):
    req = CreateProductReq(request.json)
    req.shopId = account["shop"]["id"]
    result = ProductSvc.createProduct(req)
    res = CreateProductRsp(result).serialize()
    return jsonify(res)


# @app.route('/admin/book-management/delete-book', methods=['POST'])
# def DeleteBookById():
#     req = DeleteBookByIdReq(request.json)
#     result = BookSvc.DeleteBookById(req)
#     res = DeleteBookByIdRsp(result).serialize()
#     return jsonify(res)
#
#
# @app.route('/admin/book-management/update-book', methods=['POST'])
# def UpdateBook():
#     req = UpdateBookReq(request.json)
#     result = BookSvc.UpdateBook(req)
#     res = UpdateBookRsp(result).serialize()
#     return jsonify(res)
#
#
# @app.route('/admin/book-management/get-book', methods=['POST'])
# def SearchBooks():
#     req = SearchBookReq(request.json)
#     result = BookSvc.SearchBooks(req)
#     res = SearchBookRsp(result).serialize()
#     return jsonify(res)
#
# from library import app



