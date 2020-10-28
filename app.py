import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Response
import boto3
import json

ssm = boto3.client('ssm', 
        region_name='eu-central-1'
#        endpoint_url='https://vpce-02c8ad0aa180bd28c-v38kkyx0.ssm.eu-central-1.vpce.amazonaws.com'
)
db_user = ssm.get_parameter(Name='/user_DB')
db_password = ssm.get_parameter(Name='/Pass_DB', WithDecryption=True)
db_host = 'postgredb.c7o7zikjorxv.eu-central-1.rds.amazonaws.com'
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="postgresql+psycopg2://{}:{}@{}/books_store".format(db_user['Parameter']['Value'], db_password['Parameter']['Value'], db_host)

app.config.from_object('config.DevelopmentConfig')
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
