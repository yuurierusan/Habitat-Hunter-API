import os
import secrets
import datetime
from flask import Flask
from models.db import db
from mongoengine import *
from flask_cors import CORS
from flask_restful import Api
from dotenv import load_dotenv
from flask_session import Session
from flask_jwt_extended import JWTManager
from resources.user import Users, UserById
from resources.comment import Comments, NewComment
from resources.auth import Register, Login, Logout, CheckSession
from resources.listing import Listings, ListingById, NewListing, UpdateListing, DeleteListing

load_dotenv()

# check for secret key


def get_secret_key():
    secret_key = os.environ.get('APP_SECRET_KEY')
    if not secret_key:
        secret_key = secrets.token_hex(32)
    return secret_key

# check for database connection


def connect_to_mongodb():
    MONGO_URI = os.environ.get('MONGO_URI')
    if MONGO_URI is None:
        raise ValueError("MONGO_URI environment variable is not set")


# if the secret exist call here
APP_SECRET_KEY = get_secret_key()
# if the database exist call here
MONGO_URI = os.environ.get('MONGO_URI')

app = Flask(__name__)


app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
app.config["MONGODB_SETTINGS"] = {'DB': "test", "host": MONGO_URI}
app.config['JWT_SECRET_KEY'] = APP_SECRET_KEY
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False

CORS(app, resources={r"/api/*": {"origins": "*"}})
JWTManager(app)
api = Api(app)
db.init_app(app)
Session(app)

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(Users, '/users')
api.add_resource(UserById, '/user/<id>')
api.add_resource(CheckSession, '/auth/session')
api.add_resource(Listings, '/listings')
api.add_resource(NewListing, '/listing/create')
api.add_resource(UpdateListing, '/listing/update/<id>')
api.add_resource(DeleteListing, '/listing/delete/<id>')
api.add_resource(ListingById, '/listing/<id>')
api.add_resource(Comments, '/comments')
api.add_resource(NewComment, '/comment/create')


if __name__ == "__main__":
    app.run(debug=True)
