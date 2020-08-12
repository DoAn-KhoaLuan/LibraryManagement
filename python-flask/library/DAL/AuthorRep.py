from library import db
from library.Common.Rsp.AuthorRsp import DeleteAuthorByIdRsp, UpdateAuthorRsp, SearchAuthorByIdRsp, \
    SearchAuthorByNameRsp
from library.Common.util import ConvertModelListToDictList
from library.DAL import models
from flask import jsonify, json
from library.DAL.models import Authors


def GetAuthorsByPage(req):
    author_pagination = models.Authors.query.paginate(page=req.page, per_page=req.per_page)
    has_next = author_pagination.has_next
    has_prev = author_pagination.has_prev
    authors = ConvertModelListToDictList(author_pagination.items)
    return has_next, has_prev, authors


def CreateAuthor(req):
    author = models.Authors(author_name=req.author_name)
    db.session.add(author)
    db.session.commit()
    return req


def DeleteAuthorById(req):
    author = models.Authors.query.get(req.author_id)
    db.session.delete(author)
    db.session.commit()
    res = DeleteAuthorByIdRsp(author).serialize()
    return res


def UpdateAuthor(req):
    author = models.Authors.query.get(req.author_id)
    author.author_name = req.author_name
    db.session.add(author)
    db.session.commit()
    res = UpdateAuthorRsp(author).serialize()
    return res


def SearchAuthorById(req):
    author = models.Authors.query.get(req.author_id)
    res = SearchAuthorByIdRsp(author).serialize()
    return res


def SearchAuthorByName(req):
    author = models.Authors.query.filter(models.Authors.author_name.contains(req.author_name)).all()
    authors = ConvertModelListToDictList(author)
    res = SearchAuthorByNameRsp(authors).serialize()
    return res
