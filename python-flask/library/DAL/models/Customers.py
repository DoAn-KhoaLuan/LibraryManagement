from library.app import db

class Customers(db.Model):
    customer_id
    identity_id
    account_id
    studen_code
    last_name
    first_name
    email
    phone
    birth_date
    address
    gender
    note
