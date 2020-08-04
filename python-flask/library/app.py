from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def serialize(self):
        return {"id": self.id, "title": self.title, "description": self.description}


db.create_all()


@app.route('/tasks', methods=['POST'])
def create_task():
    data=request.get_json()
    title = data['title']
    description = data['description']
    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()
    return 'sdfds'


@app.route('/tasks', methods=['GET'])
def get_task():
    return jsonify(list(map(lambda task: task.serialize(), Task.query.all())))


@app.route('/delete', methods=['DELETE'])
def delete_task():
    deletedTask = Task.query.filter_by(id=request.json["id"]).first()
    db.session.delete(deletedTask)
    db.session.commit()
    return jsonify({"result": True})


@app.route('/update', methods=['PUT'])
def update_task():
    update_task = Task.query.filter_by(id=request.json["id"]).first()
    update_task.description = request.json['description']
    update_task.title = request.json['title']
    db.session.commit()
    return jsonify({"result": True})


if __name__ == "__main__":
    app.run(debug=True)