from library.DAL import EmployeeRep


def GetEmployeesByPage(req):
    has_next, has_prev, employees = EmployeeRep.GetEmployeesbyPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "employees": employees
    }
    return result


def CreateEmployee(req):
    create_employee = EmployeeRep.CreateEmployee(req)
    return create_employee.serialize()


def UpdateEmployee(req):
    update_employee = EmployeeRep.UpdateEmployee(req)
    return update_employee.serialize()


def DeleteEmployee(req):
    delete_employee = EmployeeRep.DeleteEmployee(req)
    return delete_employee


def SearchEmployeeById(req):
    search_employee = EmployeeRep.SearchEmployeeById(req)
    return search_employee.serialize()


def SearchEmployeeByIdentityId(req):
    search_employee = EmployeeRep.SearchEmployeeIdByIdentityId(req)
    return search_employee
