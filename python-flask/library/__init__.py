import smtplib

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
CORS(app)

bcrypt = Bcrypt(app)
app.config.from_object('config')
db = SQLAlchemy(app)
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
from library import controllers



