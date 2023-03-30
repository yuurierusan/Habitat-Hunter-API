from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from resources.user import Users, SignUp, SignIn, Logout
from flask import Flask
from flask_mongoengine import MongoEngine
from resources.listing import Listings, NewListing, UpdateListing, DeleteListing
from resources.comment import Comments, NewComment
from flask_session import Session
from dotenv import load_dotenv
from flask_restful import Api
from flask_cors import CORS
from models.db import db
import datetime
import secrets
import os

load_dotenv()

APP_SECRET_KEY = secrets.token_hex(32)
MONGO_URI = os.getenv('MONGO_URI')
app = Flask(__name__)

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
app.config["MONGODB_SETTINGS"] = {'DB': "TEST", "host": MONGO_URI}
app.config['JWT_SECRET_KEY'] = APP_SECRET_KEY
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False

CORS(app)
Session(app)
jwt = JWTManager(app)
api = Api(app)
db.init_app(app, print('started'))

api.add_resource(Users, '/users')
api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(Logout, '/logout')
api.add_resource(Listings, '/listings')
api.add_resource(NewListing, '/listing/create')
api.add_resource(UpdateListing, '/listing/:id')
api.add_resource(DeleteListing, '/listing/:id')
api.add_resource(Comments, '/comments')
api.add_resource(NewComment, '/comment/create')


if __name__ == "__main__":
    app.run(debug=True)
