class CreateSupplierReq():
    def __init__(self, req):
        self.contact_name = req['contact_name']
        self.address = req['address']
        self.phone = req['phone']
        self.email = req['email']
        self.note = req['note']
        self.delete_at = req['delete_at']


class UpdateSupplierReq():
    def __init__(self, req):
        self.supplier_id = req['supplier_id']
        self.contact_name = req['contact_name']
        self.address = req['address']
        self.phone = req['phone']
        self.email = req['email']
        self.note = req['note']
        self.delete_at = req['delete_at']


class SearchSupplierByIdReq():
    def __init__(self, req):
        self.supplier_id = req['supplier_id']


class SearchSupplierByContactNameReq():
    def __init__(self, req):
        self.contact_name = req['contact_name']