class CreateProductReq(object):
    def __init__(self, req):
        self.shopId = req['shopId'] if 'shopId' in req else None
        self.categoryId = req['categoryId'] if 'categoryId' in req else None
        self.name = req['name'] if 'name' in req else None
        self.tags = req['tags'] if 'tags' in req else None
        self.retailPrice = req['retailPrice'] if 'retailPrice' in req else None
        self.costPrice = req['costPrice'] if 'costPrice' in req else None
        self.discount = req['discount'] if 'discount' in req else None
        self.rateStar = req['rateStar'] if 'rateStar' in req else None
        self.brandName = req['brandName'] if 'brandName' in req else None
        self.material = req['material'] if 'material' in req else None
        self.size = req['size'] if 'size' in req else None
        self.feature = req['feature'] if 'feature' in req else None
        self.origin = req['origin'] if 'origin' in req else None
        self.amount = req['amount'] if 'amount' in req else None
        self.rateCount = req['rateCount'] if 'rateCount' in req else None
        self.note = req['note'] if 'note' in req else None
        self.description = req['description'] if 'description' in req else None
        self.imageUrl = req['imageUrl'] if 'imageUrl' in req else None
#
#
class DeleteBookByIdReq():
    def init(self, req):
        self.bookid = req['bookid'] if 'bookid' in req else None
#
#
class UpdateProductReq():
    def init(self, req):
        self.productId = req['productId'] if 'productId' in req else None
        self.shopId = req['shopId'] if 'shopId' in req else None
        self.categoryId = req['categoryId'] if 'categoryId' in req else None
        self.name = req['name'] if 'name' in req else None
        self.tags = req['tags'] if 'tags' in req else None
        self.retailPrice = req['retailPrice'] if 'retailPrice' in req else None
        self.costPrice = req['costPrice'] if 'costPrice' in req else None
        self.discount = req['discount'] if 'discount' in req else None
        self.rateStar = req['rateStar'] if 'rateStar' in req else None
        self.brandName = req['brandName'] if 'brandName' in req else None
        self.material = req['material'] if 'material' in req else None
        self.size = req['size'] if 'size' in req else None
        self.feature = req['feature'] if 'feature' in req else None
        self.origin = req['origin'] if 'origin' in req else None
        self.amount = req['amount'] if 'amount' in req else None
        self.rateCount = req['rateCount'] if 'rateCount' in req else None
        self.note = req['note'] if 'note' in req else None
        self.description = req['description'] if 'description' in req else None
        self.imageUrl = req['imageUrl'] if 'imageUrl' in req else None
#
#
class RateProductReq:
    def __init__(self, req):
        self.star = req['star'] if 'star' in req else 0.0
        self.id = req['id'] if 'id' in req else None


