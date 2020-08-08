from flask import jsonify
from library import app
from library.BLL import BookSvc
from library.Common.Rsp.SingleRsp import SingleRsp
from flask import jsonify, json

@app.route('/', methods=['GET'])
def index():
    print("day la controller")
    allBooks = BookSvc.getAllBooks()
    print(allBooks)
    resp = SingleRsp()
    resp.create(SingleRsp.SUCCESS)
    print(resp)
    return  "jsonify(json.dumps(resp.__dict__))"
