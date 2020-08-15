from sqlalchemy import or_

from library.Common.Req import GetItemsByPageReq
from library import db
from library.Common.Req.SupplierReq import CreateSupplierReq, UpdateSupplierReq, SearchSupplierReq
from library.DAL.models import Suppliers
from library.Common.util import ConvertModelListToDictList


def GetSuppliersByPage(req: GetItemsByPageReq):
    supplier_pagination = Suppliers.query.paginate(per_page=req.per_page, page=req.page)
    has_next = supplier_pagination.has_next
    has_prev = supplier_pagination.has_prev
    suppliers = ConvertModelListToDictList(supplier_pagination.items)
    return has_next, has_prev, suppliers


def CreateSupplier(req: CreateSupplierReq):
    create_supplier = Suppliers(contact_name=req.contact_name,
                                address=req.address,
                                phone=req.phone,
                                email=req.email,
                                delete_at=req.delete_at,
                                note=req.note)
    db.session.add(create_supplier)
    db.session.commit()
    return create_supplier.serialize()


def UpdateSupplier(req: UpdateSupplierReq):
    update_supplier = Suppliers.query.get(req.supplier_id)
    update_supplier.contact_name = req.contact_name
    update_supplier.address = req.address
    update_supplier.phone = req.phone
    update_supplier.email = req.email
    update_supplier.note = req.note
    update_supplier.delete_at = req.delete_at
    db.session.add(update_supplier)
    db.session.commit()
    return update_supplier.serialize()


def SearchSupplier(req: SearchSupplierReq):
    search_supplier = Suppliers.query.filter(or_(Suppliers.supplier_id == req.keyword,
                                                 Suppliers.contact_name == req.keyword)).all()
    suppliers = ConvertModelListToDictList(search_supplier)
    return suppliers


