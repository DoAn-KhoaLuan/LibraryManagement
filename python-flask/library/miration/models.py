from library import db
from sqlalchemy.types import Enum
from library.common.util import ConvertModelListToDictList
class AccountRole(Enum):
    USER = "user"
    OWNER = "owner"
    ADMIN = "admin"

class OrderType(Enum):
    ONLINE  = "online"
    OFFLINE = "offline"

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    shops = db.relationship('Shop', backref='account')
    comments = db.relationship('Comment', backref='account', lazy='subquery')
    buyerOrders = db.relationship("Order", foreign_keys='Order.buyerAccountId', back_populates="buyerAccount")
    sellerOrders = db.relationship("Order", foreign_keys='Order.sellerAccountId', back_populates="sellerAccount")
    provinceId = db.Column(db.String(50),name="province_id")
    districtId = db.Column(db.String(50), name="district_id")
    wardId = db.Column(db.String(50), name="ward_id")
    address = db.Column(db.String(100))
    roleName = db.Column(db.Enum("user", "owner", "admin"), name="role_name", default="user")
    accountName = db.Column(db.String(50), name="account_name")
    accountPassword = db.Column(db.String(50), name="account_password")
    lastName = db.Column(db.String(50), name="last_name")
    firstName = db.Column(db.String(50), name="first_name")
    phone = db.Column(db.String(50), name="phone")
    email = db.Column(db.String(50), name="email")
    birthDate = db.Column(db.DateTime, name="birth_date")
    imageUrl = db.Column(db.String(1000), name="image_url")
    note = db.Column(db.String(1000), name="note")
    deleteAt = db.Column(db.DateTime, name="delete_at")
    createAt = db.Column(db.DateTime, name="create_at")

    def serialize(self):
        shop = None if (len(self.shops) == 0)  else self.shops[0].serialize()
        return {
            "id": self.id,
            "shop": shop,
            "provinceId": self.provinceId,
            "districtId": self.districtId,
            "wardId": self.wardId,
            "address": self.address,
            "roleName": self.roleName,
            "accountName": self.accountName,
            "lastName": self.lastName,
            "firstName": self.firstName,
            "phone": self.phone,
            "email": self.email,
            "birthDate": self.birthDate,
            "imageUrl": self.imageUrl,
            "note": self.note,
            "deleteAt": self.deleteAt,
            "createAt": self.createAt
        }


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    products = db.relationship("Product", backref="category", lazy=False)
    categoryName = db.Column(db.String(50),name="category_name")
    description = db.Column(db.String(2000), name="description")
    note = db.Column(db.String(1000), name="note")
    deleteAt = db.Column(db.DateTime, name="delete_at")
    createAt = db.Column(db.DateTime, name="create_at")

    def serialize(self):
        return {
            "id": self.id,
            "categoryName": self.categoryName,
            "description": self.description,
            "note": self.note,
            "deleteAt": self.deleteAt,
            "createAt": self.createAt,
        }


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    accountId = db.Column(db.Integer, db.ForeignKey('account.id'), name="account_id")
    productId = db.Column(db.Integer, db.ForeignKey('product.id'), name="product_id")

    title = db.Column(db.String(50),name="title")
    content = db.Column(db.String(2000))
    deleteAt = db.Column(db.DateTime, name="delete_at")
    createAt = db.Column(db.DateTime, name="create_at")

    def serialize(self):
        return {
            "id": self.id,
            "accountId": self.accountId,
            "productId": self.productId,
            "title": self.title,
            "content": self.content,
            "deleteAt": self.deleteAt,
            "createAt": self.createAt,
        }


class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    messages = db.relationship('Message', backref='conversation', lazy=True)


    isRead = db.Column(db.Boolean)
    lastMessage = db.Column(db.String(1000), name="last_message")
    deleteAt = db.Column(db.DateTime, name="delete_at")
    createAt = db.Column(db.DateTime, name="create_at")

    def serialize(self):
        return {
            "id": self.id,
            "isRead": self.isRead,
            "lastMessage": self.lastMessage,
            "deleteAt": self.deleteAt,
            "createAt": self.createAt,
        }


class District(db.Model):
    id = db.Column(db.String(10), primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(50))
    provinceId = db.Column(db.String(50), name="province_id")

    def __init__(self, id, name, provinceId) -> None:
        self.id = id
        self.name = name
        self.provinceId = provinceId
        super().__init__()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "provinceId": self.provinceId,
        }


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'), nullable=False)

    content = db.Column(db.String(2000))
    deleteAt = db.Column(db.DateTime, name="delete_at")
    createAt = db.Column(db.DateTime, name="create_at")

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "deleteAt": self.deleteAt,
            "createAt": self.createAt,

        }


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    shopId = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)

    buyerAccountId = db.Column(db.Integer, db.ForeignKey(Account.id))
    sellerAccountId = db.Column(db.Integer, db.ForeignKey(Account.id))
    #
    buyerAccount = db.relationship("Account", backref="buyerAccount", uselist=False, foreign_keys=[buyerAccountId])
    sellerAccount = db.relationship("Account", backref="sellerAccount", uselist=False, foreign_keys=[sellerAccountId])

    orderDetails = db.relationship('OrderDetail', backref="order", lazy=False)

    total = db.Column(db.Float, name="total")
    quantity = db.Column(db.Integer, name="quantity", default=0)
    type = db.Column(db.Enum("online", "offline"), name="type", default="offline")
    note = db.Column(db.String(1000), name="note")
    deleteAt = db.Column(db.DateTime, name="delete_at")
    createAt = db.Column(db.DateTime, name="create_at")

    def serialize(self):
        return {
            "id": self.id,
            "buyerAccount": self.buyerAccount.serialize(),
            "sellerAccount": self.sellerAccount.serialize(),
            "orderDetails": ConvertModelListToDictList(self.orderDetails),
            "total": self.total,
            "quantity": self.quantity,
            "type": self.type,
            "note": self.note,
            "deleteAt": self.deleteAt,
            "createAt": self.createAt,
        }


class OrderDetail(db.Model):
    orderId = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True, nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True, nullable=False)

    retailPrice = db.Column(db.Float, name="retail_price")
    total = db.Column(db.Float, name="total")
    quantity = db.Column(db.Integer, name="quantity")
    discount = db.Column(db.Float, name="discount")

    def serialize(self):
        return {
            "orderId": self.orderId,
            "productId": self.productId,
            "retailPrice": self.retailPrice,
            "total": self.total,
            "quantity": self.quantity,
            "discount": self.discount,
        }


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    categoryId = db.Column(db.Integer, db.ForeignKey("category.id"), name="category_id")
    shopId = db.Column(db.Integer, db.ForeignKey("shop.id"), name="shop_id")

    comments = db.relationship("Comment", backref="product", lazy="subquery")
    tags = db.relationship("Tag", backref="product", lazy=True)
    orderDetails = db.relationship('OrderDetail', backref='product', lazy=True)

    retailPrice = db.Column(db.Float, name="retail_price")
    costPrice = db.Column(db.Float, name="cost_price")
    discount = db.Column(db.Float, name="discount")
    rateStar = db.Column(db.Float, name="rate_star")
    name = db.Column(db.String(50), name="name")
    brandName = db.Column(db.String(50), name="brand_name")
    material = db.Column(db.String(50), name="material")
    size = db.Column(db.String(50), name="size")
    feature = db.Column(db.String(50), name="feature")
    origin = db.Column(db.String(50), name="origin")
    amount = db.Column(db.Integer, name="amount")
    rateCount = db.Column(db.Integer, name="rate_count")
    imageUrl = db.Column(db.String(1000), name="imageUrl")
    note = db.Column(db.String(1000), name="note")
    description = db.Column(db.String(2000), name="description")
    deleteAt = db.Column(db.DateTime, name="delete_at")
    createAt = db.Column(db.DateTime, name="create_at")

    def serialize(self):
        return {
            "id": self.id,
            "categoryId": self.categoryId,
            "shopId": self.shopId,
            "tags": ConvertModelListToDictList(self.tags),
            # "comments": ConvertModelListToDictList(self.comments),
            "retailPrice": self.retailPrice,
            "costPrice": self.costPrice,
            "discount": self.discount,
            "name": self.name,
            "brandName": self.brandName,
            "material": self.material,
            "size": self.size,
            "feature": self.feature,
            "origin": self.origin,
            "amount": self.amount,
            "rateCount": self.rateCount,
            "imageUrl": self.imageUrl,
            "note": self.note,
            "description": self.description,
            "deleteAt": self.deleteAt,
            "createAt": self.createAt,
        }


#
# class Author(db.Model):
#     authorAd = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
#     authorName = db.Column(db.String(50))
#
#     products = db.relationship('Product', backref='author', lazy=True)
#     deleteIdt = db.Column(db.DateTime, default=None)
#     shopId = db.Column(db.Integer, db.ForeignKey("shop.id"), name="shop_id")
#
#     def serialize(self):
#         return {"authorId": self.author_id, "authorName": self.author_name}
#
#     def __repr__(self):
#         return f"Author('{self.author_id}','{self.author_name}')"

class Province(db.Model):
    id = db.Column(db.String(10), primary_key=True, nullable=False,unique=True)
    name = db.Column(db.String(50))
    region = db.Column(db.String(50), name="region")

    def __init__(self, id, name, region) -> None:
        self.id = id
        self.name = name
        self.region = region
        super().__init__()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "region": self.region,
        }


class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    accountId = db.Column(db.Integer, db.ForeignKey("account.id"), name="account_id")

    products = db.relationship("Product", backref="shop", lazy=True)
    orders = db.relationship("Order", backref="shop", lazy=True)
    name = db.Column(db.String(200), unique=True)
    websiteUrl = db.Column(db.String(200), name="website_url")
    imageUrl = db.Column(db.String(200), name="image_url")
    address = db.Column(db.String(200), name="address")
    provinceId = db.Column(db.String(50), name="province_id")
    districtId = db.Column(db.String(50), name="district_id")
    wardId = db.Column(db.String(50), name="ward_id")
    deleteAt = db.Column(db.DateTime, name="delete_at")
    createAt = db.Column(db.DateTime, name="create_at")

    def serialize(self):
        return {
            "id": self.id,
            "accountId": self.accountId,
            "name": self.name,
            "websiteUrl": self.websiteUrl,
            "imageUrl": self.imageUrl,
            "address": self.address,
            "provinceId": self.provinceId,
            "districtId": self.districtId,
            "wardId": self.wardId,
            "deleteAt": self.deleteAt,
            "createAt": self.createAt,
        }


class Ward(db.Model):
    id = db.Column(db.String(10), primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(50))
    districtId = db.Column(db.String(50), name="district_id")

    def __init__(self, id, name, districtId) -> None:
        self.id = id
        self.name = name
        self.districtId = districtId
        super().__init__()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "districtId": self.districtId,

        }


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    productId = db.Column(db.Integer, db.ForeignKey("product.id"))
    name = db.Column(db.String(50))
    trimName = db.Column(db.String(50), name="trim_name")
    deleteAt = db.Column(db.DateTime, name="delete_at")
    createAt = db.Column(db.DateTime, name="create_at")

    def serialize(self):
        return {
            "id": self.id,
            "productId": self.productId,
            "name": self.name,
            "trimName": self.trimName,
            "deleteAt": self.deleteAt,
            "createAt": self.createAt,
        }

# class Accounts(db.Model):
#     account_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
#     account_name = db.Column(db.String(50), nullable=False, unique=True)
#     account_password = db.Column(db.String(50), nullable=False)
#     note = db.Column(db.String(50))
#     delete_at = db.Column(db.DateTime, default=None)
#     customers = db.relationship('Customers', backref='account', lazy='subquery')
#     employees = db.relationship('Employees', backref='account', lazy='subquery')
#     conversations = db.relationship('Conversations', backref='account', lazy='subquery')
#     messages = db.relationship('Messages', backref='account', lazy='subquery')
#
#     def serialize(self):
#         return {"account_id": self.account_id, "account_name": self.account_name, "note": self.note,
#                 "delete_at": self.delete_at, "role": self.role.serialize()}
#
#     def __repr__(self):
#         return f"Account('{self.account_id}','{self.account_name}','{self.note}', '{self.delete_at}', " \
#                f"'{self.role.serialize()}')"
#
#
# class Books(db.Model):
#     book_id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True, unique=True)
#     book_name = db.Column(db.String(50), nullable=False)
#     supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'))
#     category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
#     author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'))
#     old_amount = db.Column(db.Integer)
#     new_amount = db.Column(db.Integer)
#     image = db.Column(db.String(1000))
#     page_number = db.Column(db.Integer)
#     description = db.Column(db.String(1500))
#     cost_price = db.Column(db.Float)
#     retail_price = db.Column(db.Float)
#     discount = db.Column(db.Float, default=0.0)
#     ranking = db.Column(db.String(50))
#     delete_at = db.Column(db.DateTime, default=None)
#     note = db.Column(db.String(1500))
#     order_details = db.relationship('Orderdetails', backref='book', lazy=True)
#     borrow_ticket_details = db.relationship('Borrowticketdetails', backref='book', lazy=True)
#     stocktaketicketdetails = db.relationship('Stocktaketicketdetails', backref="book", lazy=True)
#
#     def serialize(self):
#         return {"book_id": self.book_id, "book_name": self.book_name, "note": self.note,
#                 "supplier": self.supplier.serialize(), "category": self.category.serialize(),
#                 "author": self.author.serialize(),
#                 "old_amount": self.old_amount, "new_amount": self.new_amount, "image": self.image,
#                 "page_number": self.page_number, "description": self.description, "cost_price": self.cost_price,
#                 "retail_price": self.retail_price, "discount": self.discount, "ranking": self.ranking,
#                 "delete_at": self.delete_at}
#
#     def __repr__(self):
#         return f"('book_id':{self.book_id},'book_name': {self.book_name},'note : {self.note},'supplier': {self.supplier.serialize()},'category': {self.category.serialize()}, " \
#                f"'author': {self.author.serialize()},'old_amount': {self.old_amount},'new_amount': {self.new_amount},'image': {self.image},'page_number': {self.page_number}, " \
#                f"'description ':{self.description},'cost_price': {self.cost_price},'retail_price': {self.retail_price},'discount': {self.discount},'ranking': {self.ranking})"
#
#
# class Borrowticketdetails(db.Model):
#     borrow_ticket_id = db.Column(db.Integer, db.ForeignKey('borrowtickets.borrow_ticket_id'), primary_key=True)
#     book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), primary_key=True)
#     delete_at = db.Column(db.DateTime, default=None)
#
#     def serialize(self):
#         return {"borrow_ticket_id": self.borrow_ticket_id, "book_id": self.book_id, "delete_at": self.delete_at, 'book': self.book.serialize()}
#
#     def __repr__(self):
#         return f"('book_id':{self.book_id}, 'borrow_ticket_id': {self.borrow_ticket_id})"
#
#
# class Borrowtickets(db.Model):
#     borrow_ticket_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
#     employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
#     quantity = db.Column(db.Integer)
#     borrow_date = db.Column(db.DateTime)
#     appointment_date = db.Column(db.DateTime)
#     return_date = db.Column(db.DateTime)
#     status = db.Column(db.Boolean)
#     delete_at = db.Column(db.DateTime, default=None)
#     note = db.Column(db.String(1500))
#     borrow_ticket_detail = db.relationship('Borrowticketdetails', backref='borrowticket', lazy=True)
#
#     def serialize(self):
#         return {"borrow_ticket_id": self.borrow_ticket_id, "customer": self.customer.serialize(), "note": self.note,
#                 "employee": self.employee.serialize(), "quantity": self.quantity, "borrow_date": self.borrow_date,
#                 "appointment_date": self.appointment_date, "return_date": self.return_date, "status": self.status,
#                 "delete_at": self.delete_at, "borrow_ticket_details": ConvertModelListToDictList(self.borrow_ticket_detail)}
#
#     def __repr__(self):
#         return f"Borrowticket('{self.borrow_ticket_id}','{self.customer.serialize()}','{self.note}','{self.employee.serialize()}'," \
#                f"'{self.quantity}','{self.borrow_date}','{self.appointment_date}','{self.return_date}','{self.status}', '{self.delete_at}')"
#
#
# class Categories(db.Model):
#     category_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
#     category_name = db.Column(db.String(50))
#     description = db.Column(db.String(1500))
#     note = db.Column(db.String(1500))
#     delete_at = db.Column(db.DateTime, default=None)
#     books = db.relationship('Books', backref="category", lazy=True)
#
#     def serialize(self):
#         return {"category_id": self.category_id, "category_name": self.category_name, "note": self.note,
#                 "description": self.description, "delete_at": self.delete_at}
#
#     def __repr__(self):
#         return f"Category('{self.category_id}','{self.category_name}','{self.note}','{self.description}', '{self.delete_at}')"
#
#
# class Customers(db.Model):
#     customer_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
#     identity_id = db.Column(db.String(50), nullable=False, unique=True)
#     account_id = db.Column(db.Integer, db.ForeignKey('accounts.account_id'), unique=True)
#     student_code = db.Column(db.String(50))
#     last_name = db.Column(db.String(50))
#     first_name = db.Column(db.String(50))
#     email = db.Column(db.String(50), unique=True)
#     phone = db.Column(db.String(50))
#     birth_date = db.Column(db.DateTime)
#     address = db.Column(db.String(1500))
#     gender = db.Column(db.Boolean)
#     note = db.Column(db.String(1500))
#     delete_at = db.Column(db.DateTime, default=None)
#     borrow_tickets = db.relationship('Borrowtickets', backref='customer', lazy=True)
#     orders = db.relationship('Orders', backref='customer', lazy=True)
#
#     def serialize(self):
#         return {"customer_id": self.customer_id, "identity_id": self.identity_id, "note": self.note,
#                 "account": self.account.serialize(), "student_code": self.student_code, "last_name": self.last_name,
#                 "first_name": self.first_name, "email": self.email, "phone": self.phone, "birth_day": self.birth_date,
#                 "address": self.address, "gender": self.gender, "delete_at": self.delete_at}
#
#     def __repr__(self):
#         return f"Customer('{self.customer_id}','{self.identity_id}','{self.note}','{self.account.serialize()}'," \
#                f"'{self.student_code}','{self.first_name}','{self.last_name}','{self.email}','{self.birth_date}','{self.address}'," \
#                f"'{self.gender}','{self.phone}', '{self.delete_at}')"
#
#
# class Conversations(db.Model):
#     conversation_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False,
#                                 unique=True)
#     customer_account_id = db.Column(db.Integer, db.ForeignKey('accounts.account_id'),
#                                      primary_key=True, nullable=False, unique=True)
#     messages = db.relationship('Messages', backref='conversation', lazy=True)
#     created_at = db.Column(db.DateTime) #Ngay khi tạo tài khoản customer thành công
#     updated_at = db.Column(db.DateTime) #Ngay khi tin nhắn gần nhất được gửi
#     last_message = db.Column(db.String(2000))
#     is_read = db.Column(db.Boolean)
#
#     def serialize(self):
#         return {'conversation_id': self.conversation_id,
#                 'customer_account_id': self.customer_account_id,
#                 'created_at': self.created_at,
#                 'updated_at': self.updated_at,
#                 'last_message': self.last_message,
#                 'account': self.account.serialize(),
#                 'is_read': self.is_read
#                 }
#
#
# class Messages(db.Model):
#     message_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False,
#                            unique=True)
#     conversation_id = db.Column(db.Integer, db.ForeignKey('conversations.conversation_id'),
#                             nullable=False)
#     content = db.Column(db.String(2000))
#     created_at = db.Column(db.DateTime)
#     deleted_at = db.Column(db.DateTime)
#     account_id = db.Column(db.Integer, db.ForeignKey('accounts.account_id'), nullable=False)
#
#     def serialize(self):
#         return {
#             'message_id': self.message_id,
#             'conversation_id': self.conversation_id,
#             'content': self.content,
#             'created_at': self.created_at,
#             'account_id': self.account_id,
#             'deleted_at': self.deleted_at,
#         }
#
#
# class Employees(db.Model):
#     employee_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
#     identity_id = db.Column(db.String(50), nullable=False, unique=True)
#     account_id = db.Column(db.Integer, db.ForeignKey('accounts.account_id'), unique=True)
#     last_name = db.Column(db.String(50), nullable=False)
#     first_name = db.Column(db.String(50), nullable=False)
#     phone = db.Column(db.String(50), nullable=False, unique=True)
#     email = db.Column(db.String(50), nullable=False, unique=True)
#     birth_date = db.Column(db.DateTime)
#     hire_date = db.Column(db.DateTime)
#     address = db.Column(db.String(1500))
#     gender = db.Column(db.Boolean)
#     image = db.Column(db.String(1500))
#     basic_rate = db.Column(db.Float)
#     note = db.Column(db.String(1500))
#     delete_at = db.Column(db.DateTime, default=None)
#     schedules = db.relationship('Schedules', backref='employee', lazy=True)
#     orders = db.relationship('Orders', backref='employee', lazy=True)
#     borrow_tickets = db.relationship('Borrowtickets', backref='employee', lazy=True)
#     stocktake_tickets = db.relationship('Stocktaketickets', backref='employee', lazy=True)
#
#     def serialize(self):
#         return {"employee_id": self.employee_id, "identity_id": self.identity_id, "note": self.note,
#                 "account": self.account.serialize(), "last_name": self.last_name, "first_name": self.first_name,
#                 "phone": self.phone, "birth_day": self.birth_date, "address": self.address, "gender": self.gender,
#                 "image": self.image, "basic_rate": self.basic_rate, "delete_at": self.delete_at, "email": self.email,
#                 "hire_date": self.hire_date}
#
#     def __repr__(self):
#         return f"Employee('{self.employee_id}','{self.identity_id}','{self.note}','{self.account.serialize()}','{self.first_name}'" \
#                f",'{self.last_name}','{self.phone}','{self.birth_date}','{self.address}','{self.gender}','{self.image}'" \
#                f",'{self.basic_rate}', '{self.delete_at}', '{self.hire_date}', '{self.email}')"
#
#
# class Orderdetails(db.Model):
#     order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), primary_key=True)
#     book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), primary_key=True)
#     retail_price = db.Column(db.Float)
#     quantity = db.Column(db.Integer)
#     discount = db.Column(db.Float)
#     total = db.Column(db.Float)
#     note = db.Column(db.String(1500))
#     delete_at = db.Column(db.DateTime, default=None)
#
#     def serialize(self):
#         return {"book": self.book.serialize(),"order_id": self.order_id, "note": self.note,
#                 "retail_price": self.retail_price, "quantity": self.quantity, "discount": self.discount,
#                 "total": self.total, "delete_at": self.delete_at}
#
#     def __repr__(self):
#         return f"Orderdetail('{self.order.serialize()}','{self.note}','{self.retail_price}','{self.quantity}'," \
#                f"'{self.discount}','{self.note}', {self.delete_at})"
#
#
# class Orders(db.Model):
#     order_id = db.Column(db.Integer, unique=True, autoincrement=True, primary_key=True, nullable=False)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
#     employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
#     order_date = db.Column(db.DateTime)
#     total = db.Column(db.Float)
#     type = db.Column(db.String(50))
#     note = db.Column(db.String(1500))
#     delete_at = db.Column(db.DateTime, default=None)
#     create_at = db.Column(db.DateTime, default=datetime.now())
#     order_details = db.relationship('Orderdetails', backref="order", lazy=False)
#
#     def serialize(self):
#         return {"order_id": self.order_id, "customer": self.customer.serialize(), "note": self.note,
#                 "employee": self.employee.serialize(), "create_at": self.create_at,
#                 "order_date": self.order_date, "total": self.total, "order_details": ConvertModelListToDictList(self.order_details),
#                 "type": self.type,
#                 "delete_at": self.delete_at}
#
#     def __repr__(self):
#         return f"Order('{self.order_id}', '{self.customer.serialize()}', '{self.employee.serialize()}','{self.note}', '{self.order_date}', '{self.total}', " \
#                f"'{self.type}', '{self.delete_at}')"
#
#
# class Roles(db.Model):
#     role_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
#     role_name = db.Column(db.String(50))
#     note = db.Column(db.String(1500))
#     delete_at = db.Column(db.DateTime, default=None)
#     accounts = db.relationship('Accounts', backref="role", lazy=True)
#
#     def serialize(self):
#         return {"role_id": self.role_id, "role_name": self.role_name, "note": self.note, "delete_at": self.delete_at}
#
#     def __repr__(self):
#         return f"Role('{self.role_id}','{self.role_name}','{self.note}', '{self.delete_at}')"
#
#
# class Schedules(db.Model):
#     schedule_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True, nullable=False)
#     employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
#     date = db.Column(db.DateTime)
#     time_from = db.Column(db.DateTime)
#     time_to = db.Column(db.DateTime)
#     actual_hours = db.Column(db.Float)
#     expected_hours = db.Column(db.Float)
#     salary = db.Column(db.Float)
#     delete_at = db.Column(db.DateTime, default=None)
#     note = db.Column(db.String(1500))
#
#     def serialize(self):
#         return {"id": self.schedule_id, "employee": self.employee.serialize(), "date": self.date,
#                 "time_from": self.time_from, "time_to": self.time_to, "note": self.note,
#                 "actual_hours": self.actual_hours, "expected_hours": self.expected_hours, "salary": self.salary,
#                 "delete_at": self.delete_at}
#
#     def __repr__(self):
#         return f"Schedule('{self.schedule_id}','{self.employee.serialize()}','{self.date}','{self.time_from}','{self.time_to}'," \
#                f"'{self.note}','{self.actual_hours}','{self.expected_hours}','{self.salary}', '{self.delete_at}')"

#
# class Stocktaketicketdetails(db.Model):
#     Stocktake_ticket_id = db.Column(db.Integer, db.ForeignKey('stocktaketickets.stocktake_ticket_id'), primary_key=True)
#     book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), primary_key=True)
#     new_quantity = db.Column(db.Integer)
#     old_quantity = db.Column(db.Integer)
#
#     def serialize(self):
#         return {"stocktake_ticket": self.stocktaketicket.serialize(), "book": self.book.serialize(),
#                 "new_quantity": self.new_quantity, "old_quantity": self.old_quantity}
#
#     def __repr__(self):
#         return f"Stocktaketicketdetail('{self.stocktaketicket.serialize()}','{self.book.serialize()}','{self.new_quantity}'," \
#                f"'{self.old_quantity}')"
#
#
# class Stocktaketickets(db.Model):
#     stocktake_ticket_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
#     employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
#     total_quantity = db.Column(db.Integer)
#     date = db.Column(db.DateTime)
#     delete_at = db.Column(db.DateTime, default=None)
#     stocktaketicketdetails = db.relationship('Stocktaketicketdetails', backref="stocktaketicket", lazy=True)
#
#     def serialize(self):
#         return {"stocktake_ticket_id": self.stocktake_ticket_id, "employee": self.employee.serialize(),
#                 "total_quantity": self.total_quantity, "date": self.date}
#
#     def __repr__(self):
#         return f"Stocktaketicket('{self.stocktake_ticket_id}','{self.employee.serialize()}','{self.total_quantity}','{self.date}', '{self.delete_at}')"
#
#
# class Suppliers(db.Model):
#     supplier_id = db.Column(db.Integer, unique=True, autoincrement=True, primary_key=True, nullable=False)
#     contact_name = db.Column(db.String(50), nullable=False)
#     address = db.Column(db.String(1500))
#     phone = db.Column(db.String(50))
#     email = db.Column(db.String(50), nullable=False)
#     note = db.Column(db.String(1500))
#     delete_at = db.Column(db.DateTime, default=None)
#     books = db.relationship('Books', backref='supplier', lazy=True)
#
#     def serialize(self):
#         return {"supplier_id": self.supplier_id, "contact_name": self.contact_name, "note": self.note,
#                 "address": self.address, "phone": self.phone, "email": self.email, "delete_at": self.delete_at}
#
#     def __repr__(self):
#         return f"Supplier('{self.supplier_id}','{self.contact_name}','{self.note}','{self.address}','{self.phone}'," \
#                f"'{self.email}', '{self.delete_at}')"
#
#
