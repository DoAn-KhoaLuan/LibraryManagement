from run import db


class Authors(db.Model):
    author_id = db.Column(db.String(50), nullable=False, primary_key = True )
    author_name = db.Column(db.String(50), nullable=False )
