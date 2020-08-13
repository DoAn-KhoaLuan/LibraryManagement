class SearchSupplierByContactNameRsp():
    def __init__(self, suppliers):
        self.suppliers = suppliers


    def serialize(self):
        return {"Supplier": self.suppliers}