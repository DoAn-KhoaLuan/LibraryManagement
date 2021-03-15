from datetime import datetime

from library import db
from library.common.Req.ShopReq import *
from miration import models
from miration.models import *


def CreateShop(req: CreateShopReq):
    shopAccount: Account = models.Account.query.filter(models.Account.id == req.accountId).first()
    shopAccount.roleName = AccountRole.OWNER
    createShop = models.Shop(
        provinceId= req.provinceId,
        districtId= req.districtId,
        wardId= req.wardId,
        address= req.address,
        accountId= req.accountId,
        name= req.name,
        imageUrl= req.imageUrl,
        createAt = datetime.now()
    )
    db.session.add(createShop, shopAccount)
    db.session.commit()
    return createShop.serialize()