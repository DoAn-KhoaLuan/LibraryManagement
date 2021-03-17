# from library.common.Rsp.SingleRsp import ErrorRsp
# from library.repository import BookRep
#
#
# def GetBooksByPage(req):
#     has_next, has_prev, books = BookRep.GetBooksByPage(req)
#     result = {
#         "has_next": has_next,
#         "has_prev": has_prev,
#         "books": books
#     }
#     if (req.per_page == 0):
#         raise ErrorRsp(code=400, message='Per page không được bằng 0')
#     return result
#
#
from library.repository import ProductRep


def createProduct(req):
    product = ProductRep.createProduct(req)
    return product
#
#
# def DeleteBookById(req):
#     book = BookRep.DeleteBookById(req)
#     return book
#
#
# def UpdateBook(req):
#     book = BookRep.UpdateBook(req)
#     return book
#
#
# def SearchBooks(req):
#     books = BookRep.SearchBooks(req)
#     return books
#
#
