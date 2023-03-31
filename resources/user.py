from flask_jwt_extended import create_access_token
from flask import request, session, jsonify, make_response
from flask_restful import Resource
from flask_bcrypt import Bcrypt
from models.user import User
from dotenv import load_dotenv
from bson import ObjectId
import os

load_dotenv()

bcrypt = Bcrypt()

SALT_ROUNDS = int(os.getenv('SALT_ROUNDS'))


def index():
    if not session.get("email"):
        return False
    return True


class Users(Resource):
    def get(self):
        users = User.objects()
        return make_response(jsonify(users), 200)


class UserById(Resource):
    def get(self, id: str):
        try:
            user = User.objects(id=ObjectId(id)).first()
            if user:
                return make_response(jsonify({'id': str(user.id), 'name': user.name, 'email': user.email}), 200)
            else:
                return {'msg': 'User not found'}, 404
        except Exception as e:
            print(f'Error retrieving user: {e}')
            return {'msg': 'Error retrieving user'}, 500


class SignUp(Resource):
    def post(self):
        user = User()
        body = request.get_json()
        password = body.get("password")
        hashed = bcrypt.generate_password_hash(password, SALT_ROUNDS)
        user.name = body.get("name")
        user.email = body.get("email")
        user.password = hashed
        user.save()
        return {"message": "User Signed Up"}, 200


class SignIn(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects(email=body.get("email")).first()
        if user:
            if bcrypt.check_password_hash(user["password"], body.get("password")):
                session['email'] = body.get('email')
                access_token = create_access_token(identity=body.get("email"))
                return make_response(jsonify(access_token=access_token, user=user, message=f"Welcome {user.name}"), 200)
            return {"message": "Unable to Login"}, 500
        return {"message": "No Such User Exist"}, 404


class Logout(Resource):
    def post(self):
        session.pop("email", None)
        return {"message": "Logged Out"}
