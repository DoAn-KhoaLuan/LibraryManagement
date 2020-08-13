from library import db
from library.Common.Req.CategoryReq import CreateCategoryReq, UpdateCategoryReq
from library.Common.util import ConvertModelListToDictList
from library.DAL import models
from flask import jsonify, json

from library.DAL.models import Categories


def GetCategoriesByPage(req):
    category_pagination = models.Categories.query.paginate(page=req.page, per_page=req.per_page)
    has_next = category_pagination.has_next
    has_prev = category_pagination.has_prev
    categories = ConvertModelListToDictList(category_pagination.items)
    return has_next, has_prev, categories


def CreateCategory(new_cate: CreateCategoryReq):
    new_category = models.Categories(category_name=new_cate.category_name, description=new_cate.description,
                                     note=new_cate.note)
    db.session.add(new_category)
    db.session.flush()
    return new_category.serialize()


def UpdateCategory(update_cate: UpdateCategoryReq):
    update_category = db.session.query(Categories).filter(Categories.category_id == update_cate.category_id).first()

    update_category.category_name = update_cate.category_name
    update_category.description = update_cate.description
    update_category.note = update_cate.note
    db.session.add(update_category)
    db.session.commit()
    return update_category.serialize()
