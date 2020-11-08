import os
import time
from random import Random, randint
# import requests
from werkzeug.utils import secure_filename

from library import app
from library.BLL import BookSvc
from library.Common.Req.GetItemsByPageReq import GetItemsByPageReq

from library.Common.Req.BookReq import CreateBookReq, DeleteBookByIdReq, UpdateBookReq, SearchBookReq

from library.Common.Rsp.BookRsp import CreateBookRsp, DeleteBookByIdRsp, UpdateBookRsp, SearchBookRsp

from library.Common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response, render_template, send_file
import json

from library.Common.Rsp.SingleRsp import ErrorRsp
from library.auth import token_required
# from library.controllers.UploadImageController import allowed_file


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


@app.route('/admin/book-management/get-book', methods=['POST'])
def SearchBooks():
    req = SearchBookReq(request.json)
    result = BookSvc.SearchBooks(req)
    res = SearchBookRsp(result).serialize()
    return jsonify(res)

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

