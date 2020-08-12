from library.DAL import AuthorRep


def GetAuthorByPage(req):
    has_next, has_prev, authors = AuthorRep.GetAuthorsByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "authors": authors
    }
    return result


def CreateAuthor(req):
    author = AuthorRep.CreateAuthor(req)
    return author


def DeleteAuthorById(req):
    author = AuthorRep.DeleteAuthorById(req)
    return author


def UpdateAuthor(req):
    author = AuthorRep.UpdateAuthor(req)
    return author


def SearchAuthorById(req):
    author = AuthorRep.SearchAuthorById(req)
    return author


def SearchAuthorByName(req):
    author = AuthorRep.SearchAuthorByName(req)
    return author