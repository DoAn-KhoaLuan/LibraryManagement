# from datetime import datetime
#
# from sqlalchemy import or_
#
# from library.common.Req import GetItemsByPageReq
# from library import db
# from library.common.Req.SupplierReq import CreateSupplierReq, UpdateSupplierReq, DeleteSupplierReq, \
#     SearchSuppliersReq
# from library.repository.models import Suppliers
# from library.common.util import ConvertModelListToDictList
#
#
# def GetSuppliersByPage(req: GetItemsByPageReq):
#     supplier_pagination = Suppliers.query.filter(Suppliers.delete_at == None).paginate(per_page=req.per_page, page=req.page)
#     hasNext = supplier_pagination.hasNext
#     hasPrev = supplier_pagination.hasPrev
#     suppliers = ConvertModelListToDictList(supplier_pagination.items)
#     return hasNext, hasPrev, suppliers
#
#
# def CreateSupplier(req: CreateSupplierReq):
#     create_supplier = Suppliers(contact_name=req.contact_name,
#                                 address=req.address,
#                                 phone=req.phone,
#                                 email=req.email,
#                                 delete_at=req.delete_at,
#                                 note=req.note)
#     db.session.add(create_supplier)
#     db.session.commit()
#     return create_supplier.serialize()
#
#
# def UpdateSupplier(req: UpdateSupplierReq):
#     update_supplier = Suppliers.query.get(req.supplier_id)
#     update_supplier.contact_name = req.contact_name
#     update_supplier.address = req.address
#     update_supplier.phone = req.phone
#     update_supplier.email = req.email
#     update_supplier.note = req.note
#     update_supplier.delete_at = req.delete_at
#     db.session.add(update_supplier)
#     db.session.commit()
#     return update_supplier.serialize()
#
#
# def SearchSuppliers(req: SearchSuppliersReq):
#     search_suppliers = Suppliers.query.filter(or_(Suppliers.supplier_id == req.supplier_id,
#                                                   Suppliers.contact_name == req.contact_name)).all()
#     suppliers = ConvertModelListToDictList(search_suppliers)
#     return suppliers
#
#
# def DeleteSupplier(req: DeleteSupplierReq):
#     delete_supplier = Suppliers.query.get(req.supplier_id)
#     delete_supplier.delete_at = datetime.now()
#     db.session.add(delete_supplier)
#     db.session.commit()
#     return delete_supplier.serialize()
