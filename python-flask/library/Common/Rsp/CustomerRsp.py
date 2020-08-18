class SearchCustomersRsp():
    def __init__(self, customers):
        self.customers = customers

    def serialize(self):
        return {"customers": self.customers}


