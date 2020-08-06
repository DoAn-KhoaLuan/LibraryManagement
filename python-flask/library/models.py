from library import db


class Accounts(db.Model):
    account_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'), nullable=False)
    account_name = db.Column(db.String(50), nullable=False)
    account_password = db.Column(db.String(50), nullable=False)
    note = db.Column(db.String(50))
    customers = db.relationship('Customers', backref='account', uselist=False)
    employees = db.relationship('Employees', backref='account', uselist=False)

    def serialize(self):
        return {"account_id": self.account_id, "account_name": self.account_name, "note": self.note,
                "account_password": self.account_password}


class Books(db.Model):
    book_id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key = True )
    book_name = db.Column(db.String(50), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id') ,nullable=False)
    old_amount = db.Column(db.Integer)
    new_amount = db.Column(db.Integer)
    image = db.Column(db.String(50))
    page_number = db.Column(db.Integer)
    description = db.Column(db.String(1500))
    cost_price = db.Column(db.Float)
    retail_price = db.Column(db.Float)
    discount = db.Column(db.Float)
    ranking = db.Column(db.String(50))
    note = db.Column(db.String(1500))

    def serialize(self):
        return {"book_id": self.book_id, "book_name": self.book_name, "note": self.note,
                "supplier_id": self.supplier_id, "category_id": self.category_id, "author_id": self.author_id,
                "old_amount": self.old_amount, "new_amount": self.new_amount, "image": self.image,
                "page_number": self.page_number, "description": self.description, "cost-price": self.cost_price,
                "retail_price": self.retail_price, "discount": self.discount, "ranking": self.ranking}




Borrowticketsdetails = db.Table('borrow_ticket_details',
                                db.Column('book_id', db.Integer, db.ForeignKey('books.book_id'), primary_key=True),
                                db.Column('borrow_ticket_id', db.Integer, db.ForeignKey('borrowtickets.borrow_ticket_id'), primary_key=True)
                                )

class Borrowtickets(db.Model):
    borrow_ticket_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), primary_key=True, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), primary_key=True, nullable=False)
    quantity = db.Column(db.Integer)
    borrow_date = db.Column(db.DateTime)
    appointment_date = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)
    status = db.Column(db.Boolean)
    note = db.Column(db.String(1500))
    books = db.relationship('Books', secondary='borrow_ticket_details', lazy='subquery', backref=db.backref('borrowticket', lazy=True))
    def serialize(self):
        return {"borrow_ticket_id": self.borrow_ticket_id, "customer_id": self.customer_id, "note": self.note,
                "employee_id": self.employee_id, "quantity": self.quantity, "borrow_date": self.borrow_date,
                "appointment_date": self.appointment_date, "return_date": self.return_date, "status": self.status}


class Categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, nullable=False)
    category_name = db.Column(db.String(50))
    description = db.Column(db.String(1500))
    note = db.Column(db.String(1500))
    books = db.relationship('Books', backref="category", lazy=True)

    def serialize(self):
        return {"category_id": self.category_id, "category_name": self.category_name, "note": self.note,
                "description": self.description}


class Customers(db.Model):
    customer_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    identity_id = db.Column(db.String(50), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.account_id'),  nullable=False, unique=True)
    student_code = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50))
    birth_date = db.Column(db.DateTime)
    address = db.Column(db.String(1500))
    gender = db.Column(db.Boolean)
    note = db.Column(db.String(1500))
    borrow_tickets = db.relationship('Borrowtickets', backref='customer', lazy=True)
    orders = db.relationship('Orders', backref='customers', lazy=True)

    def serialize(self):
        return {"customer_id": self.customer_id, "identity_id": self.identity_id, "note": self.note,
                "account_id": self.account_id, "student_code": self.student_code, "last_name": self.last_name,
                "first_name": self.first_name, "email": self.email, "phone": self.phone, "birth_day": self.birth_date,
                "address": self.address, "gender": self.gender}


class Employees(db.Model):
    employee_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    identity_id = db.Column(db.String(50), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.account_id'), nullable=False, unique=True)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.DateTime)
    hire_date = db.Column(db.DateTime)
    address = db.Column(db.String(1500))
    gender = db.Column(db.Boolean)
    image = db.Column(db.String(50))
    basic_rate = db.Column(db.Float)
    note = db.Column(db.String(1500))
    schedules = db.relationship('Schedules', backref='employee', lazy=True)
    orders = db.relationship('Orders', backref='employee', lazy=True)
    borrow_tickets = db.relationship('Borrowtickets', backref='employee', lazy=True)
    stocktake_tickets = db.relationship('Stocktaketickets', backref='employee', lazy=True)
    def serialize(self):
        return {"employee_id": self.employee_id, "identity_id": self.identity_id, "note": self.note,
                "account_id": self.account_id, "last_name": self.last_name, "first_name": self.first_name,
                "phone": self.phone, "birth_day": self.birth_date, "address": self.address, "gender": self.gender,
                "image": self.image, "basic_rate": self.basic_rate}


class Orderdetails(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    book_id = db.Column(db.Integer, primary_key=True, nullable=False)
    retail_price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    discount = db.Column(db.Float)
    total = db.Column(db.Float)
    note = db.Column(db.String(1500))

    def serialize(self):
        return {"order_id": self.order_id, "book_id": self.book_id, "note": self.note,
                "retail_price": self.retail_price, "quantity": self.quantity, "discount": self.discount,
                "total": self.note}


class Orders(db.Model):
    order_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), nullable=False)
    order_date = db.Column(db.DateTime)
    total = db.Column(db.Float)
    type = db.Column(db.String(50))
    note = db.Column(db.String(1500))

    def serialize(self):
        return {"order_id": self.order_id, "customer_id": self.customer_id, "note": self.note,
                "order_date": self.order_date, "total": self.order_date, "type": self.type}


class Roles(db.Model):
    role_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    role_name = db.Column(db.String(50))
    note = db.Column(db.String(1500))
    accounts = db.relationship('Accounts', backref="role", lazy=True)
    def serialize(self):
        return {"role_id": self.role_id, "role_name": self.role_name, "note": self.note}


class Schedules(db.Model):
    schedule_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time_from = db.Column(db.DateTime, nullable=False)
    time_to = db.Column(db.DateTime, nullable=False)
    actual_hours = db.Column(db.Float, nullable=False)
    expected_hours = db.Column(db.Float, nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {"id": self.schedule_id, "role_name": self.employee_id, "date": self.date,
                "time_from": self.time_from, "time_to": self.time_to, "note": self.note,
                "actual_hours": self.actual_hours, "expected_hours": self.expected_hours, "salary": self.salary}


class Stocktaketicketdetails(db.Model):
    Stocktake_ticket_id = db.Column(db.Integer, primary_key=True, nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    new_quantity = db.Column(db.Integer)
    old_quantity = db.Column(db.Integer)

    def serialize(self):
        return {"stocktake_ticket_id": self.Stocktake_ticket_id, "book_id": self.book_id,
                "new_quantity": self.new_quantity, "old_quantity": self.old_quantity}


class Stocktaketickets(db.Model):
    stocktake_ticket_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), primary_key=True, nullable=False)
    total_quantity = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def serialize(self):
        return {"stocktake_ticket_id": self.stocktake_ticket_id, "employee_id": self.employee_id,
                "total_quantity": self.total_quantity, "date": self.date}


class Suppliers(db.Model):
    supplier_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    contact_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(1500))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable=False)
    note = db.Column(db.String(1500))
    books = db.relationship('Books', backref='supplier', lazy=True)

    def serialize(self):
        return {"supplier_id": self.supplier_id, "contact_name": self.contact_name, "note": self.note,
                "address": self.address, "phone": self.phone, "email": self.email}


class Authors (db.Model):
    author_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    books = db.relationship('Books', backref='author', lazy=True)

    def serialize(self):
        return {"author_id": self.author_id, "first_name": self.first_name, "last_name": self.last_name}

