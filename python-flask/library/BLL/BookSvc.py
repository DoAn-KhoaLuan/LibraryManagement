from library.DAL import BookRep
def GetAllBooks(req):
    all_books = BookRep.GetAllBooks(req)
    return all_books
