from flask import jsonify
from library import app
from library.BLL import BookSvc
from library.Common.Req.PageReq import PageReq
from library.Common.Rsp.SingleRsp import SingleRsp
from flask import jsonify, json, request


@app.route('/', methods=['GET'])
def index():
    req = PageReq(request.json)
    allBooks = BookSvc.GetAllBooks(req)
    print("index")
    return allBooks



