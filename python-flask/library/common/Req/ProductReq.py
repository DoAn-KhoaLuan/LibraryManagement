class CreateProductReq(object):
    def __init__(self, req):
        self.shopId = req['shopId'] if 'shopId' in req else None
        self.categoryId = req['categoryId'] if 'categoryId' in req else None
        self.name = req['name'] if 'name' in req else None
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
# class DeleteBookByIdReq():
#     def init(self, req):
#         self.bookid = req['bookid'] if 'bookid' in req else None
#
#
# class UpdateBookReq():
#     def init(self, req):
#         self.bookid = req['bookid'] if 'bookid' in req else None
#         self.bookname = req['bookname'] if 'bookname' in req else None
#         self.supplierid = req['supplierid'] if 'supplierid' in req else 0
#         self.categoryid = req['categoryid'] if 'categoryid' in req else 0
#         self.authorid = req['authorid'] if 'authorid' in req else 0
#         self.oldamount = req['oldamount'] if 'oldamount' in req else None
#         self.newamount = req['newamount'] if 'newamount' in req else None
#         self.image = req['image'] if 'image' in req else None
#         self.pagenumber = req['pagenumber'] if 'pagenumber' in req else None
#         self.description = req['description'] if 'description' in req else None
#         self.costprice = req['costprice'] if 'costprice' in req else None
#         self.retailprice = req['retailprice'] if 'retailprice' in req else None
#         self.discount = req['discount'] if 'discount' in req else None
#         self.ranking = req['ranking'] if 'ranking' in req else None
#         self.note = req['note'] if 'note' in req else None
#
#
# class SearchBookReq:
#     def init(self, req):
#         self.bookid = req['bookid'] if 'bookid' in req else None
#         self.bookname = req['bookname'] if 'bookname' in req else None
#         self.authorid = req['authorid'] if 'authorid' in req else 0
#         self.categoryid = req['categoryid'] if 'categoryid' in req else 0
#         self.supplierid = req['supplierid'] if 'supplierid' in req else 0
