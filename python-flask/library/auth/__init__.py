from functools import wraps

import jwt
from flask import request, jsonify
from library import app
from library.BLL import AccountSvc
from library.Common.Req.AccountReq import SearchAccountsReq
from library.Common.Req.CustomerReq import SearchCustomerByAccountIdReq
from library.Common.Req.EmployeeReq import SearchEmployeeReq
from library.DAL import EmployeeRep, CustomerRep


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401
        try:
            token = auth_headers[1]
            data = jwt.decode(token, app.config['SECRET_KEY'])
            search_accounts_req = SearchAccountsReq({'account_id': data['account_id']})
            account = AccountSvc.SearchAccounts(search_accounts_req)[0]

            search_employees_req = SearchEmployeeReq({'keyword': account['account_id']})

            employee = EmployeeRep.SearchEmployees(search_employees_req)[0]

            search_customers_req = SearchCustomerByAccountIdReq({'account_id': account['account_id']})
            customer = CustomerRep.SearchCustomerByAccountId(search_customers_req)['customers'] if len(CustomerRep.SearchCustomerByAccountId(search_customers_req)['customers']) > 0 else None
            auth_info = {
                'account': account,
                'employee': employee,
                'customer': customer
            }
            return f(auth_info, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            return jsonify(invalid_msg), 401
    return _verify
