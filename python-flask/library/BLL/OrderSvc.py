from library.DAL import OrderRep


def GetOrdersByPage(req):
    has_next, has_prev, orders = OrderRep.GetOrdersbyPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "orders": orders
    }
    return result


def CreateOrder(req):
    create_order = OrderRep.CreateOrder(req)
    return create_order


def UpdateOrder(req):
    update_order = OrderRep.UpdateOrder(req)
    return update_order


def DeleteOrder(req):
    delete_order = OrderRep.DeleteOrder(req)
    return delete_order


def SearchOrderByOrderId(req):
    search_order = OrderRep.SearchOrderByOrderId(req)
    return search_order


def SearchOrderByCustomerId(req):
    search_order = OrderRep.SearchOrderByCustomerId(req)
    return search_order


def SearchOrderByEmployeeId(req):
    search_order = OrderRep.SearchOrderByEmployeeId(req)
    return search_order


def SearchOrderByOrderDate(req):
    search_order = OrderRep.SearchOrderByOrderDate(req)
    return search_order
