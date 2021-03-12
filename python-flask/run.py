from library import app, socketio

if __name__ == "__main__":
    app.debug = True
    socketio.run(app, "localhost", 8000)
