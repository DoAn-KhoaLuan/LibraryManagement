class CreateAuthorRsp():
    def __init__(self, req):
        self.author_name = req.author_name

    def serialize(self):
        return {"author_name": self.author_name}


class DeleteAuthorByIdRsp:
    def __init__(self, req):
        self.author_id = req.author_id

    def serialize(self):
        return {"author_id": self.author_id}


class UpdateAuthorRsp():
    def __init__(self, req):
        self.author_id = req.author_id
        self.author_name = req.author_name

    def serialize(self):
        return {"author_id": self.author_id, "author_name": self.author_name}


class SearchAuthorByIdRsp():
    def __init__(self, req):
        self.author_name = req.author_name

    def serialize(self):
        return {"author_name": self.author_name}


class SearchAuthorByNameRsp():
    def __init__(self, authors):
        self.authors = authors

    def serialize(self):
        return {"authors": self.authors}
