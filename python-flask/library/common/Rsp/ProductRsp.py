class CreateProductRsp():
    def __init__(self, req):
        self.id = req['id'] if 'id' in req else None
        self.categoryId = req['categoryId'] if 'categoryId' in req else None
        self.shopId = req['shopId'] if 'shopId' in req else None
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

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "shopId": self.shopId,
                "categoryId": self.categoryId,
                "retailPrice": self.retailPrice,
                "costPrice": self.costPrice,
                "discount": self.discount,
                "rateStar": self.rateStar,
                "brandName": self.brandName,
                "material": self.material,
                "size": self.size,
                "feature": self.feature,
                "origin": self.origin,
                "amount": self.amount,
                "rateCount": self.rateCount,
                "note": self.note,
                "description": self.description,
                "imageUrl": self.imageUrl,
                }


class DeleteBookByIdRsp():
    def __init__(self, req):
        self.book_id = req.book_id

    def serialize(self):
        return {"book_id": self.book_id}


class UpdateProductRsp():
    def __init__(self, req):
        self.id = req['id'] if 'id' in req else None
        self.categoryId = req['categoryId'] if 'categoryId' in req else None
        self.shopId = req['shopId'] if 'shopId' in req else None
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

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "shopId": self.shopId,
                "categoryId": self.categoryId,
                "retailPrice": self.retailPrice,
                "costPrice": self.costPrice,
                "discount": self.discount,
                "rateStar": self.rateStar,
                "brandName": self.brandName,
                "material": self.material,
                "size": self.size,
                "feature": self.feature,
                "origin": self.origin,
                "amount": self.amount,
                "rateCount": self.rateCount,
                "note": self.note,
                "description": self.description,
                "imageUrl": self.imageUrl,
                }


class SearchBookByIdRsp():
    def __init__(self, req):
        self.book_name = req.book_name
        self.supplier_id = req.supplier_id
        self.category_id = req.category_id
        self.author_id = req.author_id
        self.old_amount = req.old_amount
        self.new_amount = req.new_amount
        self.image = req.image
        self.page_number = req.page_number
        self.description = req.description
        self.cost_price = req.cost_price
        self.retail_price = req.retail_price
        self.discount = req.discount
        self.ranking = req.ranking

    def serialize(self):
        return {"book_name": self.book_name,
                "supplier_id": self.supplier_id, "category_id": self.category_id, "author_id": self.author_id,
                "old_amount": self.old_amount, "new_amount": self.new_amount, "image": self.image,
                "page_number": self.page_number, "description": self.description, "cost-price": self.cost_price,
                "retail_price": self.retail_price, "discount": self.discount, "ranking": self.ranking}


class SearchBookRsp():
    def __init__(self, books):
        self.books = books

    def serialize(self):
        return {"books": self.books}


