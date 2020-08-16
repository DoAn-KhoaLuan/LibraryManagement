class GetItemsByPageRsp():
    def __init__(self, has_next=False, has_prev=False, items=[]):
        self.has_next = has_next
        self.has_prev = has_prev
        self.items = items

    def serialize(self):
        return {
<<<<<<< HEAD
            "has_next" : self.has_next,
            "has_prev" : self.has_prev,
            "self.items" : self.items,
=======
            "has_next": self.has_next,
            "has_prev": self.has_prev,
            "items": self.items,
>>>>>>> a1b789664e1d36b5f48fbf5b79ebe6fa71b65341
        }
