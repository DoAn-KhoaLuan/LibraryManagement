from library import app
from library.BLL import BookSvc, CategorySvc
from library.Common.Req.CategoryReq import CreateCategoryReq, UpdateCategoryReq
from library.Common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.Common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response
import json

from library.Common.Rsp.SingleRsp import ErrorRsp


@app.route('/admin/category-management/get-categories', methods=['GET', 'POST'])
def GetCategories():
    req = GetItemsByPageReq(request.json)
    result = CategorySvc.GetCategoriesByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['categories']).serialize()
    return jsonify(res)


@app.route('/admin/category-management/create-category', methods=['POST'])
def CreateCategory():
    req = CreateCategoryReq(request.json)
    created_category = CategorySvc.CreateCategory(req)
    return jsonify(created_category)


@app.route('/admin/category-management/update-category', methods=['POST'])
def UpdateCategory():
    req = UpdateCategoryReq(request.json)
    updated_category = CategorySvc.UpdateCategory(req)
    return jsonify(updated_category)
