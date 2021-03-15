import json
from functools import wraps

import jwt
from flask import request, jsonify
from library import app
from library.common.Rsp.SingleRsp import ErrorRsp
from library.service import AccountSvc
from library.common.Req.AccountReq import SearchAccountsReq, LoginReq, LoginRsp
from library.common.Req.CustomerReq import SearchCustomersReq
from library.common.Req.EmployeeReq import SearchEmployeesReq
from library.repository import EmployeeRep, CustomerRep



def token_required(function):
    @wraps(function)
    def _verify():
        auth_headers = request.headers.get('Authorization', '').split()

        not_authenticated_msg = {
            'message': 'Bạn không có quyền truy cập.',
            'authenticated': False
        }

        invalid_msg = {
            'message': 'Token không hợp lệ.',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Token hết hạn sử dụng.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(not_authenticated_msg), 401
        try:
            token = auth_headers[1]
            data = jwt.decode(token, app.config['SECRET_KEY'])
            search_accounts_req = SearchAccountsReq({'account_id': data['account_id']})
            account = AccountSvc.SearchAccounts(search_accounts_req)[0]
            search_employees_req = SearchEmployeesReq({'account_id': account['account']['account_id']})
            employee = EmployeeRep.SearchEmployees(search_employees_req)[0] if len(EmployeeRep.SearchEmployees(search_employees_req)) > 0 else None

            search_customers_req = SearchCustomersReq({'account_id': account['account']['account_id']})
            customer = CustomerRep.SearchCustomers(search_customers_req)[0] if len(CustomerRep.SearchCustomers(search_customers_req)) > 0 else None

            auth_info = {
                'account': account,
                'employee': employee,
                'customer': customer
            }
            return function(auth_info)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError) as e:
            return jsonify(invalid_msg), 401
    return _verify

def admin_required(f):
    @wraps(f)
    def _verify(auth_info):
        invalid_role = {
            'message': 'Yêu cầu quyền hạn của quản trị viên',
            'authenticated': False
        }
        if(auth_info['account']['role']['role_id'] == 2):
            return f(auth_info)

        return jsonify(invalid_role), 403
    return _verify

def manager_required(f):
    @wraps(f)
    def _verify(auth_info):
        invalid_role = {
            'message': 'Yêu cầu quyền hạn của quản lí',
            'authenticated': False
        }
        if(auth_info['account']['role']['role_id'] == 1):
            return f(auth_info)

        return jsonify(invalid_role), 403
    return _verify
