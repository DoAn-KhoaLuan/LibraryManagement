from library.Common.Req.CategoryReq import CreateCategoryReq, UpdateCategoryReq
from library.DAL import CategoryRep


def GetCategoriesByPage(req):
    has_next, has_prev, categories = CategoryRep.GetCategoriesByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "categories": categories
    }
    return result

def CreateCategory(new_cate_req: CreateCategoryReq):
    new_category = CategoryRep.CreateCategory(new_cate_req)
    return new_category


def UpdateCategory(update_cate_req: UpdateCategoryReq):
    update_category = CategoryRep.UpdateCategory(update_cate_req)
    return update_category
