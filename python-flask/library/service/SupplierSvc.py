# from library.repository import SupplierRep
#
#
# def GetSupplierByPage(req):
#     hasNext, hasPrev, suppliers = SupplierRep.GetSuppliersByPage(req)
#     result = {
#         "hasNext": hasNext,
#         "hasPrev": hasPrev,
#         "suppliers": suppliers
#     }
#     return result
#
#
# def CreateSupplier(req):
#     create_supplier = SupplierRep.CreateSupplier(req)
#     return create_supplier
#
#
# def UpdateSupplier(req):
#     update_supplier = SupplierRep.UpdateSupplier(req)
#     return update_supplier
#
#
# def SearchSuppliers(req):
#     search_supplier = SupplierRep.SearchSuppliers(req)
#     return search_supplier
#
#
# def DeleteSupplier(req):
#     delete_supplier = SupplierRep.DeleteSupplier(req)
#     return delete_supplier
