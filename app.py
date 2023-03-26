from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from dotenv import load_dotenv
from flask_cors import CORS
import datetime

import os

load_dotenv()

APP_ENV = os.environ.get('APP_ENV')
DEBUG = os.environ.get('DEBUG')
MONGO_URI = os.environ.get('MONGO_URI')


app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)

CORS(app)

db = mongo.db.HabitatHunter


@app.route("/users", methods=['POST'])
def createUser():
    id = db.insert({
        'name': request.json['name'],
        'email': request.json['email'],
        'username': request.json['username']
    })
    return jsonify({'id': str(ObjectId(id)), 'msg': 'User created successfully!'})


@app.route("/owners", methods=['POST'])
def createOwner():
    id = db.insert({
        'name': request.json['name'],
        'email': request.json['email'],
        'username': request.json['username']
    })
    return jsonify({'id': str(ObjectId(id)), 'msg': 'Owner created successfully!'})


@app.route("/listings", methods=['POST'])
def createListing():
    id = db.insert({
        'image': request.json['image'],
        'title': request.json['title'],
        'price': request.json['price']
        'date': datetime.datetime.fromtimestamp(request.json['date'])
        'amenities': request.json['amenities']
    })
    return jsonify({'id': str(ObjectId(id)), 'msg': 'Listing added successfully!'})


@app.route("/comments", methods=['POST'])
def createComment():
    id = db.insert({
        'username': request.json['username'],
        'content': request.json['content'],
        'date': datetime.datetime.fromtimestamp(request.json['date'])
    })
    return jsonify({'id': str(ObjectId(id)), 'msg': 'Comment posted successfully!'})


if __name__ == "__main__":
    app.run(debug=True)
