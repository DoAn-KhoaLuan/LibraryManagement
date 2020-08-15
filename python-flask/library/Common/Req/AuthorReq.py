class CreateAuthorReq():
    def __init__(self, req):
        self.author_name = req['author_name']


class DeleteAuthorByIdReq():
    def __init__(self, req):
        self.author_id = req['author_id']


class UpdateAuthorReq():
    def __init__(self, req):
        self.author_id = req['author_id']
        self.author_name = req['author_name']


class SearchAuthorReq:
    def __init__(self, req):
        self.keyword = req['keyword'] if 'keyword' in req else None
