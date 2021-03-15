import datetime
from random import randint
from urllib import response

import requests
from flask import jsonify, request
from werkzeug.utils import secure_filename

from library import app
from library.auth import owner_required
from library.repository import LocationRep, CategoryRep
from miration.models import Category

@app.route('/test', methods=['POST'])
@owner_required
def test(account):
    return account

@app.route('/init-data', methods=['POST'])
def initData():
    loadAndInsertData()
    insertCategories()
    return "True"


@app.route('/get-provinces', methods=['POST'])
def getProvinces():
    return jsonify(LocationRep.getProvinces())


@app.route('/get-districts', methods=['POST'])
def getDistricts():
    return jsonify(LocationRep.getDistricts())


@app.route('/get-wards', methods=['POST'])
def getWards():
    return jsonify(LocationRep.getWards())


@app.route('/upload-image', methods=['POST'])
def UploadBookImage():
    print("upload ảnh nè")
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



# @app.after_request
# def after_request_func(response):
#     # return response
#     pass
#
#
#
# @app.before_request
# def before_request_func():
#     pass

def loadAndInsertData():
    provincesRes = requests.post(url="http://shop.d.etop.vn/api/etop.Location/GetProvinces", data={}, json={})
    provinces = provincesRes.json()["provinces"]

    districtsRes = requests.post(url="http://shop.d.etop.vn/api/etop.Location/GetDistricts", data={}, json={})
    districts = districtsRes.json()["districts"]

    wardsRes = requests.post(url="http://shop.d.etop.vn/api/etop.Location/GetWards", data={}, json={})
    wards = wardsRes.json()["wards"]

    for province in provinces:
        LocationRep.createProvince(province)

    for district in districts:
        LocationRep.createDistrict(district)

    for ward in wards:
        LocationRep.createWard(ward)

def insertCategories():
    categoryDicts = [
        {
            "categoryName": "Điện thoại - Máy tính bảng",
            "description": "MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "Điện tử - Điện lạnh",
            "description": "MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
        },
        {
            "categoryName": "Phụ kiện - Thiết bị số",
            "description": "MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
        },
        {
            "categoryName":"Laptop - Thiết bị IT",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note":"GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
        },
        {
            "categoryName":"Máy ảnh - Quay phim",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note":"GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
        },
        {
            "categoryName":"Điện gia dụng",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note":"GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
        },
        {
            "categoryName":"Nhà cửa đời sống",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note":"GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
        },
        {
            "categoryName":"Hàng tiêu dùng - Thực phẩm",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note":"GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
        },
        {
            "categoryName":"Đồ chơi - Mẹ & Bé",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note":"GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
        },
        {
            "categoryName":"Làm đẹp - Sức khỏe",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note":"GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
        },
        {
            "categoryName":"Thời trang - Phụ kiện",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
        },
        {
            "categoryName":"Thể thao - Dã ngoại",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
        },
        {
            "categoryName":"Xe máy, oto, xe đạp",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
        },
        {
            "categoryName":"Hàng quốc tế\", \"MÔ tả điênh thoại máy tính bảng",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
        },
        {
            "categoryName":"Sách, VPP & Qùa tặng",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
        },
        {
            "categoryName":"Voucher, Dịch vụ, Thẻ cào",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
        },
    ]
    for category in categoryDicts:
        categoryModel = Category(
                             categoryName = category['categoryName'],
                             description = category['description'],
                             note = category['note'],
                             createAt=category['createAt'],
                        )
        CategoryRep.CreateCategory(categoryModel)