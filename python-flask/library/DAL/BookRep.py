from library.Common.util import ConvertModelListToDictList
from library.DAL import models
from flask import jsonify, json


def GetBooksByPage(req):
    book_pagination = models.Books.query.paginate(page = req.page, per_page=req.per_page)
    has_next = book_pagination.has_next
    has_prev = book_pagination. has_prev
    books = ConvertModelListToDictList(book_pagination.items)

    return has_next, has_prev, books

