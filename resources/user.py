from bson import ObjectId
from models.user import User
from flask_restful import Resource
from flask import jsonify, make_response


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
