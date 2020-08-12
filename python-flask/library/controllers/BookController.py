from library import app
from library.BLL import BookSvc
from library.Common.Req.GetItemsByPageReq import GetItemsByPageReq

from library.Common.Req.BookReq import CreateBookReq, DeleteBookByIdReq, UpdateBookReq, SearchBookByIdReq, \
    SearchBookByNameReq, SearchBookByAuthorIdReq, SearchBookByCategoryIdReq, SearchBookBySupplierIdReq

from library.Common.Rsp.BookRsp import CreateBookRsp, DeleteBookByIdRsp, UpdateBookRsp, SearchBookByIdRsp, \
    SearchBookByNameRsp, SearchBookByAuthorIdRsp, SearchBookByCategoryIdRsp, SearchBookBySupplierIdRsp

from library.Common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response
import json

from library.Common.Rsp.SingleRsp import ErrorRsp


@app.route('/admin/book-management/get-books', methods=['POST'])
def GetBooks():
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


@app.route('/admin/book-management/search-book-by-id', methods=['POST'])
def SearchBookById():
    req = SearchBookByIdReq(request.json)
    result = BookSvc.SearchBookById(req)
    res = SearchBookByIdRsp(result).serialize()
    return jsonify(res)


@app.route('/admin/book-management/search-book-by-name', methods=['POST'])
def SearchBookByName():
    req = SearchBookByNameReq(request.json)
    result = BookSvc.SearchBookByName(req)

    res = SearchBookByNameRsp(result).serialize()
    return jsonify(res)


@app.route('/admin/book-management/search-book-by-author-id', methods=['POST'])
def SearchBookByAuthorId():
    req = SearchBookByAuthorIdReq(request.json)
    result = BookSvc.SearchBookByAuthorId(req)
    res = SearchBookByAuthorIdRsp(result).serialize()
    return jsonify(res)


@app.route('/admin/book-management/search-book-by-category-id', methods=['POST'])
def SearchBookByCategoryId():
    req = SearchBookByCategoryIdReq(request.json)
    result = BookSvc.SearchBookByCategoryId(req)
    res = SearchBookByCategoryIdRsp(result).serialize()
    return jsonify(res)


@app.route('/admin/book-management/search-book-by-supplier-id', methods=['POST'])
def SearchBookBySupplierId():
    req = SearchBookBySupplierIdReq(request.json)
    result = BookSvc.SearchBookBySupplierId(req)
    res = SearchBookBySupplierIdRsp(result).serialize()
    return jsonify(res)
