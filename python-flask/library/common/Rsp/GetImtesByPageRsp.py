class GetItemsByPageRsp():
    def __init__(self, hasNext=False, hasPrev=False, items=[], currentPage=None):
        self.hasNext = hasNext
        self.hasPrev = hasPrev
        self.items = items
        self.current_page = currentPage if currentPage else None

    def serialize(self):
        return {
            "hasNext": self.hasNext,
            "hasPrev": self.hasPrev,
            "items": self.items,
            "current_page": self.current_page,
        }
