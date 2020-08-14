class SearchCustomerByIdentityIdRsp():
    def __init__(self, customers):
        self.customers = customers

    def serialize(self):
        return {"customers ": self.customers}


class SearchCustomerByAccountIdRsp():
    def __init__(self, customers):
        self.customers = customers

    def serialize(self):
        return {"customers ": self.customers}


class SearchCustomerByPhoneRsp():
    def __init__(self, customers):
        self.customers = customers

    def serialize(self):
        return {"customers ": self.customers}
