from datetime import datetime
#
from sqlalchemy import or_
#
# from library import db
# from library.common.Req.BookReq import SearchBookReq, CreateBookReq
# from library.repository import models
# from library.common.util import ConvertModelListToDictList
#
#

#
#

from library import db
from library.common.Req import GetItemsByPageReq
from library.common.Req.PageReq import DeleteItemReq, SearchItemsReq
from library.common.util import ConvertModelListToDictList
from library.miration import models
from library.common.Req.ProductReq import CreateProductReq, UpdateProductReq, RateProductReq
from library.miration.models import Tag


def createProduct(req: CreateProductReq):
    product = models.Product(
                        shopId=req.shopId,
                        categoryId=req.categoryId,
                        retailPrice=req.retailPrice,
                        costPrice=req.costPrice,
                        discount=req.discount,
                        rateStar=0.0,
                        name=req.name,
                        brandName=req.brandName,
                        material=req.material,
                        size=req.size,
                        feature=req.feature,
                        origin=req.origin,
                        amount=req.amount,
                        rateCount=0,
                        imageUrl=req.imageUrl,
                        note=req.note,
                        description=req.description,
                        createAt=datetime.now(),
    )

    db.session.add(product)
    db.session.commit()
    for tag in req.tags:
        tag = Tag(name=tag['name'], trimName=tag['trimName'], createAt=datetime.now())
        product.tags.append(tag)
        db.session.commit()
    return product.serialize()


def getProductsByPage(req: GetItemsByPageReq):
    productPagination = models.Product.query.filter(
        (models.Product.deleteAt == None),
        (models.Product.shopId == req.shopId)
            )\
        .paginate(page=req.page, per_page=req.perPage)
    hasNext = productPagination.has_next
    hasPrev = productPagination.has_prev
    products = ConvertModelListToDictList(productPagination.items)
    return hasNext, hasPrev, products


def updateProduct(req: UpdateProductReq):
    updateProduct = models.Product.query.get(req.productId)
    updateProduct.shopId=req.shopId,
    updateProduct.categoryId=req.categoryId,
    updateProduct.retailPrice=req.retailPrice,
    updateProduct.costPrice=req.costPrice,
    updateProduct.discount=req.discount,
    updateProduct.name=req.name,
    updateProduct.brandName=req.brandName,
    updateProduct.material=req.material,
    updateProduct.size=req.size,
    updateProduct.feature=req.feature,
    updateProduct.origin=req.origin,
    updateProduct.amount=req.amount,
    updateProduct.imageUrl=req.imageUrl,
    updateProduct.note=req.note,
    updateProduct.description=req.description,
    db.session.add(updateProduct)
    db.session.commit()
    return updateProduct
#
#
def searchProducts(req: SearchItemsReq, byShop = True):
    if byShop:
        modelProducts = models.Product.query.filter(or_(
                models.Product.id == req.id,
                models.Product.name == req.name,
                models.Product.categoryId == req.categoryId,
            ),
            models.Product.shopId == req.shopId,
            models.Product.deleteAt == None,
        ).all()
    else:
        modelProducts = models.Product.query.filter(or_(
            models.Product.id == req.id,
            models.Product.name == req.name,
            models.Product.categoryId == req.categoryId,
            ),
            models.Product.deleteAt == None,
            ).all()
    products = ConvertModelListToDictList(modelProducts)
    return products


def deleteProduct(req: DeleteItemReq):
    product = models.Product.query.get(req.id)
    product.deleteAt = datetime.now()
    db.session.add(product)
    db.session.commit()
    return product.serialize()


def rateProduct(req: RateProductReq):
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
