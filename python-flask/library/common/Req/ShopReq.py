class CreateShopReq:
    def __init__(self, req):
        self.accountId = req['accountId'] if 'accountId' in req else ''
        self.name = req['name'] if 'name' in req else ''
        self.imageUrl = req['imageUrl'] if 'imageUrl' in req else ''
        self.address = req['address'] if 'address' in req else ''
        self.provinceId = req['provinceId'] if 'provinceId' in req else ''
        self.districtId = req['districtId'] if 'districtId' in req else ''
        self.wardId = req['wardId'] if 'wardId' in req else ''
        self.provinceId = req['provinceId'] if 'provinceId' in req else ''
        self.note = req['note'] if 'note' in req else ''
