from flask import request

from library.auth import user_required
from library.common.Req.ShopReq import *
from library.service import ShopSvc
from library import app

@app.route('/admin/shop-management/create-shop', methods=['POST'])
@user_required
def CreateShop(account):
    req = CreateShopReq(request.json)
    req.accountId = account["id"]
    result = ShopSvc.CreateShop(req)
    return result
