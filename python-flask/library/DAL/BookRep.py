from library.DAL import models
from flask import jsonify, json
def GetAllBooks():
    print("day la lop Rep")
    allBooks = models.Books.query.all()
    # print(jsonify(list(map(lambda task: task.serialize(), models.Books.query.all()))))
    return jsonify(list(map(lambda task: task.serialize(), allBooks)))
