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
    return create_employee


def UpdateEmployee(req):
    update_employee = EmployeeRep.UpdateEmployee(req)
    return update_employee


def DeleteEmployee(req):
    delete_employee = EmployeeRep.DeleteEmployee(req)
    return delete_employee


def SearchEmployeeById(req):
    search_employee = EmployeeRep.SearchEmployeeById(req)
    return search_employee.serialize()


def SearchEmployeeByIdentityId(req):
    search_employee = EmployeeRep.SearchEmployeeIdByIdentityId(req)
    return search_employee


def SearchEmployeeByAccountId(req):
    search_employee = EmployeeRep.SearchEmployeeIdByAccountId(req)
    return search_employee


def SearchEmployeeByName(req):
    search_employee = EmployeeRep.SearchEmployeeIdByName(req)
    return search_employee

def SearchEmployeeByPhone(req):
    search_employee = EmployeeRep.SearchEmployeeIdByPhone(req)
    return search_employee
