from library import app, socketio
from library.controller.AppController import initData

if __name__ == "__main__":
    # initData()
    app.debug = True
    # app.run(debug=True)
    socketio.run(app, "localhost", 5000)
