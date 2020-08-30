from datetime import datetime

from sqlalchemy import or_

from library import db
from library.Common.Req.BookReq import SearchBookReq
from library.DAL import models
from flask import jsonify, json
from library.Common.util import ConvertModelListToDictList


def GetBooksByPage(req):
    book_pagination = models.Books.query.filter(models.Books.delete_at == None).paginate(page=req.page, per_page=req.per_page)
    has_next = book_pagination.has_next
    has_prev = book_pagination.has_prev
    books = ConvertModelListToDictList(book_pagination.items)
    print(type(books))
    return has_next, has_prev, books


def CreateBook(req):
    book = models.Books(
                        book_name=req.book_name,
                        supplier_id=req.supplier_id,
                        category_id=req.category_id,
                        author_id=req.author_id,
                        old_amount=req.old_amount,
                        new_amount=req.new_amount,
                        image=req.image,
                        page_number=req.page_number,
                        description=req.description,
                        cost_price=req.cost_price,
                        retail_price=req.retail_price,
                        discount=req.discount,
                        ranking=req.ranking)

    db.session.add(book)
    db.session.commit()
    return book


def DeleteBookById(req):
    book = models.Books.query.get(req.book_id)
    book.delete_at = datetime.now()
    db.session.add(book)
    db.session.commit()
    return book.serialize()


def UpdateBook(req):
    book = models.Books.query.get(req.book_id)
    book.book_name = req.book_name if req.book_name is not None else book.book_name
    book.supplier_id = req.supplier_id if  req.supplier_id is not None else book.supplier_id
    book.category_id = req.category_id if req.category_id is not None else book.category_id
    book.author_id = req.author_id if req.author_id is not None else book.author_id
    book.old_amount = req.old_amount if req.old_amount is not None else book.old_amount
    book.new_amount = req.new_amount if req.new_amount is not None else book.new_amount
    book.image = req.image if req.image is not None else book.image
    book.page_number = req.page_number if req.page_number is not None else book.page_number
    book.description = req.description if req.description is not None else book.description
    book.cost_price = req.cost_price if req.cost_price is not None else book.cost_price
    book.retail_price = req.retail_price if req.retail_price is not None else book.retail_price
    book.discount = req.discount if req.discount is not None else book.discount
    book.ranking = req.ranking if req.ranking is not None else book.ranking
    book.note = req.note if req.note is not None else book.note
    db.session.add(book)
    db.session.commit()
    return book


def SearchBook(req: SearchBookReq):
    model_books = models.Books.query.filter(or_(
            models.Books.book_id == req.book_id,
            models.Books.book_name == req.book_name,
            models.Books.author_id == req.author_id,
            models.Books.category_id == req.category_id,
            models.Books.supplier_id == req.supplier_id,
    )).all()
    books = ConvertModelListToDictList(model_books)
    return books
