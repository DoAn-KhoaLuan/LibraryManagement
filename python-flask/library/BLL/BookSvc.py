from library.Common.Rsp.SingleRsp import ErrorRsp
from library.DAL import BookRep
def GetBooksByPage(req):
    has_next, has_prev, books = BookRep.GetBooksByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "books": books
    }
    if(req.per_page == 0):
        raise ErrorRsp(code=400, message='Per page không được bằng 0')
    return result
