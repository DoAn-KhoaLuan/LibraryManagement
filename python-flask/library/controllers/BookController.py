import os
import time
from random import Random, randint
# import requests
from werkzeug.utils import secure_filename

from library import app, db
from library.BLL import BookSvc
from library.DAL import models
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq

from library.common.Req.BookReq import CreateBookReq, DeleteBookByIdReq, UpdateBookReq, SearchBookReq

from library.common.Rsp.BookRsp import CreateBookRsp, DeleteBookByIdRsp, UpdateBookRsp, SearchBookRsp

from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response, render_template, send_file
import json

from library.common.Rsp.SingleRsp import ErrorRsp
# from library.controllers.UploadImageController import allowed_file


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


@app.route('/admin/book-management/search-books', methods=['POST'])
def SearchBooks():
    req = SearchBookReq(request.json)
    result = BookSvc.SearchBooks(req)
    res = SearchBookRsp(result).serialize()
    return jsonify(res)

@app.route('/admin/book-management/get-book-by-id', methods=['POST'])
def GetBookByID():
    req = SearchBookReq(request.json)
    result = models.Books.query.filter(models.Books.book_id == req.book_id)

    return jsonify(result.first().serialize())

@app.route('/admin/book-management/upload-book-image', methods=['POST'])
def UploadBookImage():
    import cloudinary.uploader
    file = request.files['image']
    tail_image = file.filename.split('.')[1]
    filename = secure_filename(str(randint(1,10000000000000))+'.'+tail_image)
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) // luu file anhr vào thư mục
    cloudinary.config(
        cloud_name = app.config['CLOUD_NAME'],
        api_key = app.config['API_KEY'],
        api_secret = app.config['API_SECRET']
    )

    res = cloudinary.uploader.upload(file, public_id=filename.split('.')[0], width=600, height=900, crop="lfill") #filename la local path cua image, public_id la tên lưu trên cloudinary
    cloudinary.utils.cloudinary_url("sample_remote.jpg")
    return jsonify({'image': res['url']})


class RateBooktReq:
    def __init__(self, req):
        self.star = req['star'] if 'star' in req else 0.0
        self.id = req['id'] if 'id' in req else None

@app.route('/admin/book-management/rate-product', methods=['POST'])
def rateProduct():
    req= RateBooktReq(request.json)
    rateProduct: models.Product = models.Product.query.get(req.id)

    oldStar = rateProduct.rateStar
    oldCount = rateProduct.rateCount
    newStar = req.star

    avgStar = ((oldStar * oldCount) + newStar) / (oldCount + 1)
    rateProduct.rateStar = avgStar
    rateProduct.rateCount = oldCount + 1

    db.session.add(rateProduct);
    db.session.commit()
    return rateProduct.serialize()
