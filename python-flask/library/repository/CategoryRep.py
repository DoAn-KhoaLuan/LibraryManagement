# from datetime import datetime
#
# from sqlalchemy import or_
#
# from library import db
# from library.common.Req.CategoryReq import CreateCategoryReq, UpdateCategoryReq, DeleteCategoryByIdReq, \
#     SearchCategoryReq
#
# from library.common.util import ConvertModelListToDictList
# from library.repository import models
# from flask import jsonify, json
#
# from library.repository.models import Categories
#
#
from library.common.util import ConvertModelListToDictList
from library.miration import models


def getCategories():
    category_pagination = models.Category.query.all()
    categories = ConvertModelListToDictList(category_pagination)
    return categories
#
#
from library import db


def CreateCategory(newCate):
    db.session.add(newCate)
    db.session.commit()
    return newCate.serialize()
#
#
# def UpdateCategory(update_cate: UpdateCategoryReq):
#     update_category = db.session.query(Categories).filter(Categories.category_id == update_cate.category_id).first()
#     update_category.category_name = update_cate.category_name
#     update_category.description = update_cate.description
#     update_category.note = update_cate.note
#     db.session.add(update_category)
#     db.session.commit()
#     return update_category.serialize()
#
#
# def DeleteCategoryById(req: DeleteCategoryByIdReq):
#     delete_category = models.Categories.query.get(req.category_id)
#     delete_category.delete_at = datetime.now()
#     db.session.add(delete_category)
#     db.session.commit()
#     return delete_category.serialize()
#
#
# def SearchCategory(req: SearchCategoryReq):
#     search_category = models.Categories.query.filter(or_(models.Categories.category_id == req.category_id,
#                                                          models.Categories.category_name == req.category_name)).all()
#     categories = ConvertModelListToDictList(search_category)
#     return categories
#
#
