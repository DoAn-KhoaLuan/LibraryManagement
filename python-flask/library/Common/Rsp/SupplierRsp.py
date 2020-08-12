class SearchSupplierByContactNameRsp():
    def __init__(self, contact_name):
        self.contact_name = contact_name


    def serialize(self):
        return {"Supplier": self.contact_name}