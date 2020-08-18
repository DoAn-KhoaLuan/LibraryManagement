from library.Common.Rsp.SingleRsp import ErrorRsp
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
    try:
        create_order = OrderRep.CreateOrder(req)
        return create_order
    except ErrorRsp as e:
        raise e


def UpdateOrder(req):
    update_order = OrderRep.UpdateOrder(req)
    return update_order


def DeleteOrder(req):
    delete_order = OrderRep.DeleteOrder(req)
    return delete_order


def SearchOrders(req):
    search_order = OrderRep.SearchOrders(req)
    return search_order


