from library.DAL import models
from flask import jsonify, json
def GetAllBooks(req):
    print("rep")
    allBooks = models.Books.query.paginate(page = req.page, per_page=req.per_page).items
    return jsonify(list(map(lambda task: task.serialize(), allBooks)))
