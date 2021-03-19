# from datetime import datetime
#
# from sqlalchemy import or_
#
# from library import db
# from library.common.Req.AuthorReq import SearchAuthorReq
# from library.common.Rsp.AuthorRsp import DeleteAuthorByIdRsp, UpdateAuthorRsp,SearchAuthorRsp
# from library.common.util import ConvertModelListToDictList
# from library.repository import models
# from flask import jsonify, json
# from library.repository.models import Authors
#
#
# def GetAuthorsByPage(req):
#     author_pagination = models.Authors.query.filter(models.Authors.delete_at == None).paginate(page=req.page, per_page=req.per_page)
#     hasNext = author_pagination.hasNext
#     hasPrev = author_pagination.hasPrev
#     authors = ConvertModelListToDictList(author_pagination.items)
#     return hasNext, hasPrev, authors
#
#
# def CreateAuthor(req):
#     author = models.Authors(author_name=req.author_name)
#     db.session.add(author)
#     db.session.commit()
#     return author
#
#
# def DeleteAuthorById(req):
#     author = models.Authors.query.get(req.author_id)
#     author.delete_at = datetime.now()
#     db.session.add(author)
#     db.session.commit()
#     res = DeleteAuthorByIdRsp(author).serialize()
#     return res
#
#
# def UpdateAuthor(req):
#     author = models.Authors.query.get(req.author_id)
#     author.author_name = req.author_name
#     db.session.add(author)
#     db.session.commit()
#     res = UpdateAuthorRsp(author).serialize()
#     return res
#
#
# def SearchAuthor(req: SearchAuthorReq):
#     author = models.Authors.query.filter(or_(models.Authors.author_id == req.author_id,
#                                              models.Authors.author_name == req.author_name)).all()
#     authors = ConvertModelListToDictList(author)
#
#     return authors
