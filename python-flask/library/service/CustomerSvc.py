# from library.repository import CustomerRep
#
#
# def GetCustomersByPage(req):
#     hasNext, hasPrev, customers = CustomerRep.GetCustomersByPage(req)
#     result = {
#         "hasNext": hasNext,
#         "hasPrev": hasPrev,
#         "customers": customers
#     }
#     return result
#
#
# def CreateCustomer(req):
#     create_customer = CustomerRep.CreatCustomer(req)
#     return create_customer
#
#
# def UpdateCustomer(req):
#     update_customer = CustomerRep.UpdateCustomer(req)
#     return update_customer
#
#
# def DeleteCustomer(req):
#     delete_customer = CustomerRep.DeleteCustomer(req)
#     return delete_customer
#
#
# def SearchCustomers(req):
#     search_customer = CustomerRep.SearchCustomers(req)
#     return search_customer
#
#
