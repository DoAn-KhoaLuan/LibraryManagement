from datetime import datetime

from sqlalchemy import or_

from library.Common.Req import GetItemsByPageReq
from library import db
from library.Common.Req.SupplierReq import CreateSupplierReq, UpdateSupplierReq, DeleteSupplierReq, \
    SearchSuppliersReq
from library.DAL.models import Suppliers
from library.Common.util import ConvertModelListToDictList


def GetSuppliersByPage(req: GetItemsByPageReq):
    supplier_pagination = Suppliers.query.filter(Suppliers.delete_at == None).paginate(per_page=req.per_page, page=req.page)
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
    update_supplier.contact_name = req.contact_name if req.contact_name is not None else update_supplier.contact_name
    update_supplier.address = req.address if req.address is not None else update_supplier.address
    update_supplier.phone = req.phone if req.phone is not None else update_supplier.phone
    update_supplier.email = req.email if req.email is not None else update_supplier.email
    update_supplier.note = req.note if req.note is not None else update_supplier.note
    update_supplier.delete_at = req.delete_at if req.delete_at is not None else update_supplier.delete_at
    db.session.commit()
    return update_supplier.serialize()


def SearchSuppliers(req: SearchSuppliersReq):
    search_suppliers = Suppliers.query.filter(or_(Suppliers.supplier_id == req.supplier_id,
                                                  Suppliers.contact_name == req.contact_name)).all()
    suppliers = ConvertModelListToDictList(search_suppliers)
    return suppliers


def DeleteSupplier(req: DeleteSupplierReq):
    delete_supplier = Suppliers.query.get(req.supplier_id)
    delete_supplier.delete_at = datetime.now()
    db.session.add(delete_supplier)
    db.session.commit()
    return delete_supplier.serialize()
