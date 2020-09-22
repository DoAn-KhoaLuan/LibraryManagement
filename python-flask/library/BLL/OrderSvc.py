import hashlib
import hmac
import json
import urllib
import uuid

from library.Common.Req.OrderReq import CreateOrderReq
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

def CreateOrderByMomo(req: CreateOrderReq):
    print(req)
    endpoint = "https://test-payment.momo.vn/gw_payment/transactionProcessor"
    partnerCode = "MOMOY1ZA20200907" #busssiness momo
    accessKey = "rVuWIV2U6YHmb803"#busssiness momo
    serectkey = "EQeEkD4sirbclirmqPv5qXDrcLu2h5EZ"#busssiness momo
    orderInfo = "pay with MoMo" #hieenj lên thông tin info
    returnUrl = "http://localhost:4200/admin/pos-management" # redicrect sau đi hoàn tất thanh toán
    notifyUrl = "http://localhost:5000/admin/order-management/test-create-order-momo"
    amount = str(req.total) #Số tiền của hóa đơn
    orderId = str(uuid.uuid4()) # order id của momo chứ ko phải của chúng ta
    requestId = str(uuid.uuid4()) # như trên
    requestType = "captureMoMoWallet"
    extraData = "merchantName=;merchantId="

    rawSignature = "partnerCode=" + partnerCode + "&accessKey=" + accessKey + "&requestId=" + requestId + "&amount=" + str(amount) + "&orderId=" + orderId + "&orderInfo=" + orderInfo + "&returnUrl=" + returnUrl + "&notifyUrl=" + notifyUrl + "&extraData=" + extraData


    h = hmac.new(serectkey.encode('utf-8'), rawSignature.encode('utf-8'), hashlib.sha256)
    signature = h.hexdigest()


    data = {
        'partnerCode': partnerCode,
        'accessKey': accessKey,
        'requestId': requestId,
        'amount': amount,
        'orderId': orderId,
        'orderInfo': orderInfo,
        'returnUrl': returnUrl,
        'notifyUrl': notifyUrl,
        'extraData': extraData,
        'requestType': requestType,
        'signature': signature
    }

    data = json.dumps(data)

    clen = len(data)
    req = urllib.request.Request(endpoint,data.encode('utf-8'),
                                 {'Content-Type': 'application/json', 'Content-Length': clen}
                                 )
    f = urllib.request.urlopen(req)

    response = f.read()
    f.close()
    print(response)
    return json.loads(response)

def UpdateOrder(req):
    update_order = OrderRep.UpdateOrder(req)
    return update_order


def DeleteOrder(req):
    delete_order = OrderRep.DeleteOrder(req)
    return delete_order


def SearchOrders(req):
    search_order = OrderRep.SearchOrders(req)
    return search_order


