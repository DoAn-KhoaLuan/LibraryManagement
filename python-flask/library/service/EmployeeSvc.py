# from library.repository import EmployeeRep
#
#
# def GetEmployeesByPage(req):
#     hasNext, hasPrev, employees = EmployeeRep.GetEmployeesbyPage(req)
#     result = {
#         "hasNext": hasNext,
#         "hasPrev": hasPrev,
#         "employees": employees
#     }
#     return result
#
#
# def CreateEmployee(req):
#     create_employee = EmployeeRep.CreateEmployee(req)
#     return create_employee
#
#
# def UpdateEmployee(req):
#     update_employee = EmployeeRep.UpdateEmployee(req)
#     return update_employee
#
#
# def DeleteEmployee(req):
#     delete_employee = EmployeeRep.DeleteEmployee(req)
#     return delete_employee
#
#
# def SearchEmployee(req):
#     search_employee = EmployeeRep.SearchEmployees(req)
#     return search_employee
#
