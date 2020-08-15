class SearchBorrowTicketRsp():
    def __init__(self, borrowtickets):
        self.borrowtickets = borrowtickets

    def serialize(self):
        return {"borrowtickets": self.borrowtickets}
