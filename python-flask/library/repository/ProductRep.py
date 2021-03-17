from datetime import datetime
#
# from sqlalchemy import or_
#
# from library import db
# from library.common.Req.BookReq import SearchBookReq, CreateBookReq
# from library.repository import models
# from library.common.util import ConvertModelListToDictList
#
#
# def GetBooksByPage(req):
#     book_pagination = models.Books.query.filter(models.Books.delete_at == None).paginate(page=req.page, per_page=req.per_page)
#     has_next = book_pagination.has_next
#     has_prev = book_pagination.has_prev
#     books = ConvertModelListToDictList(book_pagination.items)
#     return has_next, has_prev, books
#
#
from library import db
from library.common.Req.ProductReq import CreateProductReq
from miration import models


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
    return product.serialize()
#
#
# def DeleteBookById(req):
#     book = models.Books.query.get(req.book_id)
#     book.delete_at = datetime.now()
#     db.session.add(book)
#     db.session.commit()
#     return book.serialize()
#
#
# def UpdateBook(req):
#     book = models.Books.query.get(req.book_id)
#     book.book_name = req.book_name
#     book.supplier_id = req.supplier_id
#     book.category_id = req.category_id
#     book.author_id = req.author_id
#     book.old_amount = req.old_amount
#     book.new_amount = req.new_amount
#     book.image = req.image
#     book.page_number = req.page_number
#     book.description = req.description
#     book.cost_price = req.cost_price
#     book.retail_price = req.retail_price
#     book.discount = req.discount
#     book.ranking = req.ranking
#     book.note = req.note
#     db.session.add(book)
#     db.session.commit()
#     return book
#
#
# def SearchBooks(req: SearchBookReq):
#     if(req.book_id):
#         model_books = models.Books.query.filter(models.Books.book_id == req.book_id)
#         return ConvertModelListToDictList(model_books)
#
#     model_books = models.Books.query.filter(or_(
#             models.Books.book_name.contains(req.book_name),
#             # models.Books.author_id == req.author_id,
#             # models.Books.category_id == req.category_id,
#             # models.Books.supplier_id == req.supplier_id,
#     )).all()
#     print(model_books)
#     books = ConvertModelListToDictList(model_books)
#     return books
