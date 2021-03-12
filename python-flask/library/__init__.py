import smtplib
from datetime import time

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO, send, emit, join_room, leave_room

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
app.config.from_object('config')
app.debug = True
app.host = 'localhost'
app.port = 8080
db = SQLAlchemy(app)
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
socketio = SocketIO(app, cors_allowed_origins="*")
from library import controller


