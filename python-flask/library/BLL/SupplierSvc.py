from library.DAL import SupplierRep


def GetSupplierByPage(req):
    has_next, has_prev, suppliers = SupplierRep.GetSuppliersByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "suppliers": suppliers
    }
    return result


def CreateSupplier(req):
    create_supplier = SupplierRep.CreateSupplier(req)
    return create_supplier


def UpdateSupplier(req):
    update_supplier = SupplierRep.UpdateSupplier(req)
    return update_supplier


def SearchSupplierById(req):
    search_supplier = SupplierRep.SearchSupplierById(req)
    return search_supplier

def  SearchSupplierByContactName(req):
    search_supplier = SupplierRep.SearchSupplierByContactName(req)
    return search_supplier
