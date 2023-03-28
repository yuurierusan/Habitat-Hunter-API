from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from resources.user import Users, SignUp, SignIn, Logout
from flask import Flask, request, session, jsonify
from flask_mongoengine import MongoEngine
from resources.listing import Listing
from resources.comment import Comment
from flask_session import Session
from dotenv import load_dotenv
from flask_restful import Api
from flask_cors import CORS
from models.db import db
import datetime
import os

load_dotenv()

APP_SECRET_KEY = os.getenv('APP_SECRET_KEY')
MONGO_URI = os.getenv('MONGO_URI')
app = Flask(__name__)

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
app.config["MONGODB_SETTINGS"] = {'DB': "TEST", "host": MONGO_URI}
app.config['JWT_SECRET_KEY'] = APP_SECRET_KEY
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False

CORS(app)
Session(app)
api = Api(app)
db.init_app(app, print('started'))

api.add_resource(Users, '/users')
api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(Logout, '/logout')

if __name__ == "__main__":
    app.run(debug=True)
