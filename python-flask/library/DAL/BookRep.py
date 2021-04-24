from datetime import datetime

from sqlalchemy import or_

from library import db
from library.common.Req.BookReq import SearchBookReq, CreateBookReq
from library.DAL import models
from library.common.util import ConvertModelListToDictList


def GetBooksByPage(req):
    book_pagination = models.Books.query.filter(models.Books.delete_at == None).paginate(page=req.page, per_page=req.per_page)
    has_next = book_pagination.has_next
    has_prev = book_pagination.has_prev
    books = ConvertModelListToDictList(book_pagination.items)
    return has_next, has_prev, books


def CreateBook(req: CreateBookReq):
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
    book.book_name = req.book_name
    book.supplier_id = req.supplier_id
    book.category_id = req.category_id
    book.author_id = req.author_id
    book.old_amount = req.old_amount
    book.new_amount = req.new_amount
    book.image = req.image
    book.page_number = req.page_number
    book.description = req.description
    book.cost_price = req.cost_price
    book.retail_price = req.retail_price
    book.discount = req.discount
    book.ranking = req.ranking
    book.note = req.note
    db.session.add(book)
    db.session.commit()
    return book


def SearchBooks(req: SearchBookReq):
    if(req.book_id):
        model_books = models.Books.query.filter(models.Books.book_id == req.book_id)
        return ConvertModelListToDictList(model_books)

    all_books = models.Books.query
    if req.book_name != None:
        all_books = all_books.filter(models.Books.book_name.contains(req.book_name))

    if req.category_id != None:
        all_books = all_books.filter(models.Books.category_id.contains(req.category_id))

    if req.supplier_id != None:
            all_books = all_books.filter(models.Books.supplier_id.contains(req.supplier_id))

    books = ConvertModelListToDictList(all_books.all())
    return books

