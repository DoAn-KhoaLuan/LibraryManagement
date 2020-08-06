from library.DAL import BookRep
def getAllBooks():
    print("day la lớp service")
    allBooks = BookRep.GetAllBooks()
    return allBooks
