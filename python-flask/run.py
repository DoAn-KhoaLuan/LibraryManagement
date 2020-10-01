from library import app, socketio

if __name__ == "__main__":
    app.debug = True
    app.host = 'localhost'
    app.port = 5000
    socketio.run(app)
