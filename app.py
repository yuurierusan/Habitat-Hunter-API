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

APP_SECRET_KEY = secrets.token_hex(32)
MONGO_URI = os.environ.get('MONGO_URI')
app = Flask(__name__)

CORS(app)
Session(app)
JWTManager(app)
api = Api(app)
db.init_app(app)

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
app.config["MONGODB_SETTINGS"] = {'DB': "Habitat-Hunter", "host": MONGO_URI}
app.config['JWT_SECRET_KEY'] = APP_SECRET_KEY
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False


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
    app.run()
