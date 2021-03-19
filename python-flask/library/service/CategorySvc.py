# from library.common.Req.CategoryReq import CreateCategoryReq, UpdateCategoryReq, DeleteCategoryByIdReq, SearchCategoryReq
# from library.repository import CategoryRep
#
#
# def GetCategoriesByPage(req):
#     hasNext, hasPrev, categories = CategoryRep.GetCategoriesByPage(req)
#     result = {
#         "hasNext": hasNext,
#         "hasPrev": hasPrev,
#         "categories": categories
#     }
#     return result
#
#
# def CreateCategory(new_cate_req: CreateCategoryReq):
#     new_category = CategoryRep.CreateCategory(new_cate_req)
#     return new_category
#
#
# def UpdateCategory(update_cate_req: UpdateCategoryReq):
#     update_category = CategoryRep.UpdateCategory(update_cate_req)
#     return update_category
#
#
# def DeleteCategoryById(req: DeleteCategoryByIdReq):
#     delete_category = CategoryRep.DeleteCategoryById(req)
#     return delete_category
#
# def SearchCategory(req: SearchCategoryReq):
#     search_category = CategoryRep.SearchCategory(req)
#     return search_category
#
