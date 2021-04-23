import json

from library import app, db
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq, GetShopItemById
from library.common.Req.PageReq import DeleteItemReq, SearchItemsReq
from library.common.Req.ProductReq import *
from library.miration import models
from library.miration.models import Account
from library.service import ProductSvc

from library.common.Rsp.ProductRsp import DeleteBookByIdRsp, SearchBookRsp, CreateProductRsp, UpdateProductRsp

from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request

from library.common.Rsp.SingleRsp import ErrorRsp
from library.auth import user_required, owner_required


# from library.controller.UploadImageController import allowed_file

@app.route('/admin/product-management/get-shop-product-by-id', methods=['POST'])
@owner_required
def GetShopProductById(account: Account ):
    req = GetShopItemById(request.json)
    req.shopId = account["shop"]["id"]
    modelProduct = models.Product.query.filter(
        (models.Product.id == req.id),
        (models.Product.deleteAt == None),
        (models.Product.shopId == req.shopId)
            ).first()

    return jsonify(modelProduct.serialize())



@app.route('/admin/product-management/get-products-by-shop', methods=['POST'])
@owner_required
def GetProductsByPage(account):
    try:
        req = GetItemsByPageReq(request.json)
        req.shopId = account["shop"]["id"]
        result = ProductSvc.getProductsByPage(req)
        res = GetItemsByPageRsp(hasNext=result['hasNext'], hasPrev=result['hasPrev'],
                                items=result['products']).serialize()
        return jsonify(res)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8')
#
#
@app.route('/admin/product-management/create-product', methods=['POST'])
@owner_required
def CreateProduct(account):
    req = CreateProductReq(request.json)
    req.shopId = account["shop"]["id"]
    result = ProductSvc.createProduct(req)
    res = CreateProductRsp(result).serialize()
    return jsonify(res)

@app.route('/admin/product-management/update-product', methods=['POST'])
@owner_required
def UpdateProduct(account):
    req = UpdateProductReq(request.json)
    req.shopId = account["shop"]["id"]
    updateProduct = models.Product.query.get(req.id)
    updateProduct.categoryId = req.categoryId,
    updateProduct.retailPrice = req.retailPrice,
    updateProduct.costPrice = req.costPrice,
    updateProduct.discount = req.discount,
    updateProduct.name = req.name,
    updateProduct.brandName = req.brandName,
    updateProduct.material = req.material,
    updateProduct.size = req.size,
    updateProduct.feature = req.feature,
    updateProduct.origin = req.origin,
    updateProduct.amount = req.amount,
    updateProduct.imageUrl = req.imageUrl,
    updateProduct.note = req.note,
    updateProduct.description = req.description,
    db.session.add(updateProduct)
    db.session.commit()
    return jsonify(updateProduct.serialize())

@app.route('/admin/product-management/delete-product', methods=['POST'])
def deleteProduct():
    req = DeleteItemReq(request.json)
    result = ProductSvc.deleteProduct(req)
    res = DeleteItemReq(result).serialize()
    return jsonify(res)
#
#
@app.route('/admin/product-management/search-shop-products', methods=['POST'])
@owner_required
def searchProductsByShopShop(account):
    req = SearchItemsReq(request.json)
    req.shopId = account["shop"]["id"]
    result = ProductSvc.searchProductsByShop(req)
    res = GetItemsByPageRsp(items=result).serialize()
    return jsonify(res)


@app.route('/admin/product-management/search-products', methods=['POST'])
@owner_required
def searchProducts(account):
    req = SearchItemsReq(request.json)
    result = ProductSvc.searchProducts(req)
    res = GetItemsByPageRsp(items=result).serialize()
    return jsonify(res)


@app.route('/admin/product-management/rate-product', methods=['POST'])
def rateProduct():
    req = RateProductReq(request.json)
    result = ProductSvc.rateProduct(req)
    return jsonify(result)
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



