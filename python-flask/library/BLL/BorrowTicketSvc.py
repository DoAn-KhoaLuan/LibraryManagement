from library.Common.Req.BorrowTicketReq import CreateBorrowTicketReq
from library.Common.Rsp.SingleRsp import ErrorRsp
from library.DAL import BorrowTicketRep


def GetBorrowTicketsByPage(req):
    has_next, has_prev, borrow_tickets = BorrowTicketRep.GetBorrowTicketsByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "borrow_tickets": borrow_tickets
    }
    return result


def CreateBorrowTicket(req: CreateBorrowTicketReq):
    try :
        create_borrow_ticket = BorrowTicketRep.CreateBorrowTicket(req)
        return create_borrow_ticket
    except ErrorRsp as e:
        raise e


def UpdateBorrowTicket(req):
    update_borrow_ticket = BorrowTicketRep.UpdateBorrowTicket(req)
    return update_borrow_ticket


def FinishBorrowTicket(req):
    update_borrow_ticket = BorrowTicketRep.FinishBorrowTicket(req)
    return update_borrow_ticket

def DeleteBorrowTicket(req):
    delete_borrow_ticket = BorrowTicketRep.DeleteBorrowTicket(req)
    return delete_borrow_ticket


def SearchBorrowTicket(req):
    search_borrow_ticket = BorrowTicketRep.SearchBorrowTicket(req)
    return search_borrow_ticket
