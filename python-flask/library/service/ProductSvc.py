# from library.common.Rsp.SingleRsp import ErrorRsp
# from library.repository import BookRep
#
#
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.common.Req.PageReq import SearchItemsReq
from library.common.Req.ProductReq import RateProductReq
from library.common.Rsp.SingleRsp import ErrorRsp
from library.repository import ProductRep


def getProductsByPage(req: GetItemsByPageReq):
    hasNext, hasPrev, products = ProductRep.getProductsByPage(req)
    result = {
        "hasNext": hasNext,
        "hasPrev": hasPrev,
        "products": products
    }
    if (req.perPage == 0):
        raise ErrorRsp(code=400, message='Per page không được bằng 0')
    return result




def createProduct(req):
    product = ProductRep.createProduct(req)
    return product
#
#
def deleteProduct(req):
    book = ProductRep.deleteProduct(req)
    return book
#
#
def updateProduct(req):
    product = ProductRep.updateProduct(req)
    return product
#
#
def searchProducts(req: SearchItemsReq):
    products = ProductRep.searchProducts(req)
    return products
#
#
def rateProduct(req: RateProductReq):
    product = ProductRep.rateProduct(req)
    return product
