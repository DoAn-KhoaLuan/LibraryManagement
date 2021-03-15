from flask import request

from library.common.Req.ShopReq import *
from library.service import ShopSvc
from library import app

@app.route('/admin/shop-management/create-shop', methods=['POST'])
def CreateShop():
    req = CreateShopReq(request.json)
    result = ShopSvc.CreateShop(req)
    return result