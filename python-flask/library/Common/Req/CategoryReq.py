class CreateCategoryReq(object):
    def __init__(self, req):
        self.category_name = req['category_name']
        self.description = req['description']
        self.note = req['note']


class UpdateCategoryReq(object):
    def __init__(self, req):
        self.category_id = req['category_id']
        self.category_name = req['category_name']
        self.description = req['description']
        self.note = req['note']


class DeleteCategoryByIdReq():
    def __init__(self, req):
        self.category_id = req['category_id']


class SearchCategoryReq():
    def __init__(self, req):
        self.keyword = req['keyword'] if 'keyword' in req else None




