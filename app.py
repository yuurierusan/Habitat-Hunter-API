from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import Flask, request, session, jsonify
from resources.user import Users, SignUp, SignIn, Logout
from flask_mongoengine import MongoEngine
from resources.listing import Listing
from resources.comment import Comment
from flask_session import Session
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask_restful import Api
from flask_cors import CORS
from models.db import db

import os

load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')

app = Flask(__name__)

app.config["MONGO_URI"] = MONGO_URI
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

CORS(app)
Session(app)
api = Api(app)
db.init_app(app)

api.add_resource(Users, '/users')
api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(Logout, '/logout')

if __name__ == "__main__":
    app.run(debug=True)
