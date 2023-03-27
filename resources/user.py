from flask import request, session, jsonify, make_response
from flask_restful import Resource
from flask_bcrypt import Bcrypt
from models.user import User

bcrypt = Bcrypt()


def index():
    if not session.get("email"):
        return False
    return True


class Users(Resource):
    def get(self):
        users = User.objects()
        return make_response(jsonify(users), 200)

    def get_user_by_id(id: str):
        if index():
            current_user = get_jwt_identity()
            user = User.objects(email=current_user).first()
            id = User.objects(id=id)
            if user and id:
                return jsonify(id), 200
            return {'msg': 'Unable to find account'}, 404
        return {'msg': 'Log In '}, 404


class SignUp(Resource):
    def post(self):
        user = User()
        body = request.get_json()
        email = User.objects(email=body.get("email")).first()
        count = User.objects.count()
        if email or count == 1:
            return {"message": "Email already exists"}, 500
        hashed = bcrypt.generate_password_hash(body.get("password"), 10)
        user.email = body.get("email")
        user.password = hashed
        user.save()
        return {"message": "User created"}, 200


class SignIn(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects(email=body.get("email")).first()
        if user and user.password == body.get("password"):
            session['email'] = body.get('email')
            return make_response(jsonify(user), 200)
        return {"msg": "User doesn't exist or password is incorrect"}


class Logout(Resource):
    def post(self):
        session.pop("email", None)
        return {"message": "Logged Out"}
