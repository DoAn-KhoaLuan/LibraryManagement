from datetime import datetime

from library import db
from library.DAL import LocationRep, CategoryRep, models, AccountRep
from library.DAL.models import Roles, Customers
from library.common.Req.AccountReq import CreateEmployeeAccountReq
from library.controllers import BookController
from library.controllers import CategoryController
from library.controllers import AccountController
from library.controllers import AuthorController, SupplierController, EmployeeController, CustomerController, \
    OrderController, ScheduleController, BorrowTicketController, OrderDetailController, RevenueController, UploadImageController,MessageController, LoginController
import requests

def loadAndInsertData():
    provincesRes = requests.post(url="http://shop.d.etop.vn/api/etop.Location/GetProvinces", data={}, json={})
    provinces = provincesRes.json()["provinces"]

    districtsRes = requests.post(url="http://shop.d.etop.vn/api/etop.Location/GetDistricts", data={}, json={})
    districts = districtsRes.json()["districts"]

    wardsRes = requests.post(url="http://shop.d.etop.vn/api/etop.Location/GetWards", data={}, json={})
    wards = wardsRes.json()["wards"]

    for province in provinces:
        LocationRep.createProvince(province)

    for district in districts:
        LocationRep.createDistrict(district)

    for ward in wards:
        LocationRep.createWard(ward)



def insertCategories():
    categoryDicts = [
        {
            "categoryName": "Sách tư duy - Kỹ năng sống",
            "description": "MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
        },
        {
            "categoryName": "Tiểu thuyết",
            "description": "MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
        },
        {
            "categoryName": "Kiến thức - Bách khoa",
            "description": "MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
        },
        {
            "categoryName":"Sách kỹ năng làm việc",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note":"GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
        },
        {
            "categoryName":"Sách nghệ thuật sách đẹp",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note":"GHI CHÚ MÁY TINH BẢNG",
            "createAt":datetime.now(),
        },
        {
            "categoryName": "Sách tư liệu",
            "description": "MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
        },
        {
            "categoryName":"Sách, VPP & Qùa tặng",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
        },
        {
            "categoryName":"Voucher, Dịch vụ, Thẻ cào",
            "description":"MÔ tả điênh thoại máy tính bảng",
            "note": "GHI CHÚ MÁY TINH BẢNG",
            "createAt": datetime.now(),
        },
    ]
    for category in categoryDicts:
        categoryModel = models.Categories(
                             category_name = category['categoryName'],
                             description = category['description'],
                             note = category['note'],
                        )
        CategoryRep.CreateCategory(categoryModel)

def initAdminAccount():
    req = CreateEmployeeAccountReq({
        "role_id": 1,
        "account_name": "admin",
        "account_password":"123456789",
        # Employee
        "identity_id": "078088006138",
        "last_name": "Nguyễn Văn",
        "first_name": "Kim Hải",
        "phone": "0865248526",
        "email": "1751012015hai@ou.edu.vn",
        "address": "381 Nguyễn Kiệm",
        "gender": True,
        "image":"",
        "basic_rate": 50000,
        "note": "Tài khoản admin đầu tiên của chương trình",
    })
    account, employee = AccountRep.CreateEmployeeAccount(req)



def initRoles():
    role1 = Roles(role_id=1, role_name="admin");
    role2 = Roles(role_id=2,role_name= "admin-manager");
    role3 = Roles(role_id=3, role_name="user");
    db.session.add(role1)
    db.session.add(role2)
    db.session.add(role3)
    db.session.commit()

def initAnomyCustomer():
    indepentCustomer = Customers(customer_id=1, identity_id=0, first_name="Khách lẻ")
    db.session.add(indepentCustomer)
    db.session.commit()


