class SearchEmployeeByIdentityIdRsp():
    def __init__(self, employees):
        self.employees = employees

    def serialize(self):
        return {"employees ": self.employees}


class SearchEmployeeByAccountIdRsp():
    def __init__(self, employees):
        self.employees = employees

    def serialize(self):
        return {"employees ": self.employees}


class SearchEmployeeByNameRsp():
    def __init__(self, employees):
        self.employees = employees

    def serialize(self):
        return {"employees ": self.employees}


class SearchEmployeeByPhoneRsp():
    def __init__(self, employees):
        self.employees = employees

    def serialize(self):
        return {"employees ": self.employees}
