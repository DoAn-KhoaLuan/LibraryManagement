from flask import jsonify
from library import app
from library.BLL import BookSvc

@app.route('/', methods=['GET'])
def index():
    print("day la controller")
    allBooks = BookSvc.getAllBooks()
    return allBooks
