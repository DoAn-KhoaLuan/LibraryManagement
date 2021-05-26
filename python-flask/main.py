
from library import app, socketio

if __name__ == "__main__":
    app.debug = True
    # app.run(debug=True, host='0.0.0.0')
    socketio.run(app, "localhost", 5000)
