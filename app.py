import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import env_file
from flask import Response



env_file.load('.env')
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Book

@app.route("/health")
def health():
    try:
        book=Book.query.all
        return (str(200), 200)
    except Exception as e:
	    return(str(e), 500)

@app.route("/hello")
def hello():
    return ("Hello World!", 200)

@app.route("/add")
def add_book():
    name=request.args.get('name')
    author=request.args.get('author')
    published=request.args.get('published')
    try:
        book=Book(
            name=name,
            author=author,
            published=published
        )
        db.session.add(book)
        db.session.commit()
        return ("Book added. book id={}".format(book.id), 201)
    except Exception as e:
	    return(str(e), 500)

@app.route("/list")
def get_all():
    try:
        books=Book.query.all()
        return  jsonify([e.serialize() for e in books])
    except Exception as e:
	    return(str(e), 500)
    return render_template("index.html", title="List of Book"), 200

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        book=Book.query.filter_by(id=id_).first()
        return jsonify(book.serialize(), 200)
    except Exception as e:
	    return(str(e), 500)

if __name__ == '__main__':
    app.run()