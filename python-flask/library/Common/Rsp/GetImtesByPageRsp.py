class GetItemsByPageRsp():
    def __init__(self, has_next=False, has_prev=False, items=[]):
        self.has_next = has_next
        self.has_prev = has_prev
        self.items = items

    def serialize(self):
        return {
            "has_next" : self.has_next,
            "has_prev" : self.has_prev,
            "self.items" : self.items,
        }
