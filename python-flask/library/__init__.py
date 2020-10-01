import smtplib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
app.config.from_object('config')
db = SQLAlchemy(app)
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
socketio = SocketIO(app, cors_allowed_origins="*")
from library import controllers

@socketio.on('connect')
def test_connect():
    print('connexct ')
    send('connect')

@socketio.on('event')
def test_connect(data):
    print('event ', data)
    emit('event',data)
