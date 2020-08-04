from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import Flask, render_template
import pymysql
import secrets

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app = Flask(__name__)
app.config['SECRETS_KEY'] = 'superSecretsKey'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    def __repr__(self):
        return"id: {0} | first_name: {1} | last_name: {2}".format(self.id, self.first_name, self.last_name)


@app.route("/")
def index():
    book = Books(first_name="nha gia kim", last_name="abc")
    db.session.add(book)
    db.session.commit()
    return "hello world"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
