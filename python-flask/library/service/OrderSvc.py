import hashlib
import hmac
import json
import urllib
import uuid

from library.common.Req.OrderReq import CreateOrderReq
from library.common.Rsp.SingleRsp import ErrorRsp
from library.repository import OrderRep
#
#
def GetOrdersByPage(req):
    hasNext, hasPrev, orders = OrderRep.GetOrdersbyPage(req)

    result = {
        "hasNext": hasNext,
        "hasPrev": hasPrev,
        "orders": orders
    }
    return result
#
#
def createOrder(req):
    try:
        createOrder = OrderRep.createOrder(req)
        return createOrder
    except ErrorRsp as e:
        raise e
#
# def CreateOrderByMomo(req: CreateOrderReq):
#     endpoint = "https://test-payment.momo.vn/gw_payment/transactionProcessor"
#     partnerCode = "MOMOY1ZA20200907" #busssiness momo
#     accessKey = "rVuWIV2U6YHmb803"#busssiness momo
#     serectkey = "EQeEkD4sirbclirmqPv5qXDrcLu2h5EZ"#busssiness momo
#     orderInfo = "Thanh toán bằng Momo" #hieenj lên thông tin info
#     returnUrl = "http://localhost:4200/admin/pos-management" # redicrect sau đi hoàn tất thanh toán
#     notifyUrl = "http://localhost:5000/admin/order-management/test-create-order-momo"
#     amount = str(req.total) #Số tiền của hóa đơn
#     orderId = str(uuid.uuid4()) # order id của momo chứ ko phải của chúng ta
#     requestId = str(uuid.uuid4()) # như trên
#     requestType = "captureMoMoWallet"
#     extraData = "merchantName=;merchantId="
#
#     rawSignature = "partnerCode=" + partnerCode + "&accessKey=" + accessKey + "&requestId=" + requestId + "&amount=" + str(amount) + "&orderId=" + orderId + "&orderInfo=" + orderInfo + "&returnUrl=" + returnUrl + "&notifyUrl=" + notifyUrl + "&extraData=" + extraData
#
#     h = hmac.new(serectkey.encode('utf-8'), rawSignature.encode('utf-8'), hashlib.sha256)
#     signature = h.hexdigest()
#
#
#     data = {
#         'partnerCode': partnerCode,
#         'accessKey': accessKey,
#         'requestId': requestId,
#         'amount': amount,
#         'orderId': orderId,
#         'orderInfo': orderInfo,
#         'returnUrl': returnUrl,
#         'notifyUrl': notifyUrl,
#         'extraData': extraData,
#         'requestType': requestType,
#         'signature': signature
#     }
#
#     data = json.dumps(data)
#
#     clen = len(data)
#     req = urllib.request.Request(endpoint,data.encode('utf-8'),
#                                  {'Content-Type': 'application/json', 'Content-Length': clen}
#                                  )
#     f = urllib.request.urlopen(req)
#
#     response = f.read()
#     f.close()
#     return json.loads(response)
#
# def UpdateOrder(req):
#     update_order = OrderRep.UpdateOrder(req)
#     return update_order
#
#
def deleteOrder(req):
    deleteOrder = OrderRep.deleteOrder(req)
    return deleteOrder
#
#
def searchOrdersByShop(req):
    search_orders = OrderRep.searchOrdersByShop(req)
    return search_orders
#
#
