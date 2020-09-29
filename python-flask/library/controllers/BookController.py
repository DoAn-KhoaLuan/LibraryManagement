from library import app
from library.BLL import BookSvc
from library.Common.Req.GetItemsByPageReq import GetItemsByPageReq

from library.Common.Req.BookReq import CreateBookReq, DeleteBookByIdReq, UpdateBookReq, SearchBookReq

from library.Common.Rsp.BookRsp import CreateBookRsp, DeleteBookByIdRsp, UpdateBookRsp, SearchBookRsp

from library.Common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response
import json

from library.Common.Rsp.SingleRsp import ErrorRsp
from library.auth import token_required


@app.route('/admin/book-management/get-books', methods=['POST'])
@token_required
def GetBooks(auth_info):
    try:
        req = GetItemsByPageReq(request.json)
        result = BookSvc.GetBooksByPage(req)
        res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                                items=result['books']).serialize()
        return jsonify(res)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8')


@app.route('/admin/book-management/create-book', methods=['POST'])
def CreateBook():
    req = CreateBookReq(request.json)
    result = BookSvc.CreateBook(req)
    res = CreateBookRsp(result).serialize()
    return jsonify(res)


@app.route('/admin/book-management/delete-book', methods=['POST'])
def DeleteBookById():
    req = DeleteBookByIdReq(request.json)
    result = BookSvc.DeleteBookById(req)
    res = DeleteBookByIdRsp(result).serialize()
    return jsonify(res)


@app.route('/admin/book-management/update-book', methods=['POST'])
def UpdateBook():
    req = UpdateBookReq(request.json)
    result = BookSvc.UpdateBook(req)
    res = UpdateBookRsp(result).serialize()
    return jsonify(res)


@app.route('/admin/book-management/search-books', methods=['POST'])
def SearchBook():
    req = SearchBookReq(request.json)
    result = BookSvc.SearchBook(req)
    res = SearchBookRsp(result).serialize()
    return jsonify(res)


