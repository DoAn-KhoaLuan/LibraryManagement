from library.common.Req.ShopReq import CreateShopReq
from library.repository import ShopRep


def CreateShop(req: CreateShopReq):
    res = ShopRep.CreateShop(req)
    return res