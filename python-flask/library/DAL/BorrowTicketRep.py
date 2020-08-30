from sqlalchemy import or_

from library import db
from library.Common.Req.BorrowTicketReq import CreateBorrowTicketReq, UpdateBorrowTicketReq, DeleteBorrowTicketReq, \
    SearchBorrowTicketReq
from library.DAL import models
from flask import jsonify, json
from library.Common.util import ConvertModelListToDictList
from library.Common.Req import GetItemsByPageReq
from datetime import datetime


def GetBorrowTicketsByPage(req: GetItemsByPageReq):
    borrowticket_pagination = models.Borrowtickets.query.filter(models.Borrowtickets.delete_at == None).paginate \
        (per_page=req.per_page, page=req.page)
    has_next = borrowticket_pagination.has_next
    has_prev = borrowticket_pagination.has_prev
    borrow_tickets = ConvertModelListToDictList(borrowticket_pagination.items)
    return has_next, has_prev, borrow_tickets


def CreateBorrowTicket(req: CreateBorrowTicketReq):
    create_borrow_ticket = models.Borrowtickets(customer_id=req.customer_id,
                                                employee_id=req.employee_id,
                                                quantity=req.quantity,
                                                borrow_date=req.borrow_date,
                                                appointment_date=req.appointment_date,
                                                return_date=req.return_date,
                                                status=req.status,
                                                delete_at=req.delete_at,
                                                note=req.note)
    db.session.add(create_borrow_ticket)
    db.session.commit()
    return create_borrow_ticket.serialize()


def UpdateBorrowTicket(req: UpdateBorrowTicketReq):
    update_borrow_ticket = models.Borrowtickets.query.get(req.borrow_ticket_id)
    update_borrow_ticket.customer_id = req.customer_id if req.customer_id is not None else update_borrow_ticket.customer_id
    update_borrow_ticket.employee_id = req.employee_id if req.employee_id is not None else update_borrow_ticket.employee_id
    update_borrow_ticket.quantity = req.quantity if req.quantity is not None else update_borrow_ticket.quantity
    update_borrow_ticket.borrow_date = req.borrow_date if req.borrow_date is not None else update_borrow_ticket.borrow_date
    update_borrow_ticket.appointment_date = req.appointment_date if req.appointment_date is not None else update_borrow_ticket.appointment_date
    update_borrow_ticket.return_date = req.return_date if req.return_date is not None else update_borrow_ticket.return_date
    update_borrow_ticket.status = req.status if req.status is not None else update_borrow_ticket.status
    update_borrow_ticket.delete_at = req.delete_at if req.delete_at is not None else update_borrow_ticket.delete_at
    update_borrow_ticket.note = req.note if req.note is not None else update_borrow_ticket.note
    db.session.commit()
    return update_borrow_ticket.serialize()


def DeleteBorrowTicket(req: DeleteBorrowTicketReq):
    delete_borrow_ticket = models.Borrowtickets.query.get(req.borrow_ticket_id)
    delete_borrow_ticket.delete_at = datetime.now()
    db.session.add(delete_borrow_ticket)
    db.session.commit()
    return delete_borrow_ticket.serialize()


def SearchBorrowTicket(req: SearchBorrowTicketReq):
    search_borrow_ticket = models.Borrowtickets.query.filter(or_(models.Borrowtickets.customer_id == req.keyword,
                                                                 models.Borrowtickets.employee_id == req.keyword,
                                                                 models.Borrowtickets.borrow_date == req.keyword,
                                                                 models.Borrowtickets.return_date == req.keyword,
                                                                 models.Borrowtickets.status == req.keyword)).all()
    borrow_tickets = ConvertModelListToDictList(search_borrow_ticket)
    return borrow_tickets
