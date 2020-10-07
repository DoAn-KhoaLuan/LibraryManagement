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
db = SQLAlchemy(app)
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
socketio = SocketIO(app, cors_allowed_origins="*")
from library import controllers

@socketio.on('incoming-msg')
def on_message(data):
    """Broadcast messages"""
    msg = data["msg"]
    auth_info = data["auth_info"]
    room = data["room"]
    send({"auth_info": auth_info, "msg": msg}, room=room)


@socketio.on('join')
def on_join(data):
    """User joins a room"""
    session['auth_info']=data['auth_info']
    room = data["room"]
    join_room(room)

    send({"msg" : "Someone has joined the " + room + " room."}, room=room)


@socketio.on('leave')
def on_leave(data):
    """User leaves a room"""
    room = data['room']
    leave_room(room)
    send({"msg":"Someone has left the room"}, room=room)
