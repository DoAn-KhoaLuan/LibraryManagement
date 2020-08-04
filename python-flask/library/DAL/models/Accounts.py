from library.app import db

class Accounts(db.Model):
    account_id
    role_id
    account_name
    account_password
    note
