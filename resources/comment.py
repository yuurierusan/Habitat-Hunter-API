from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, jsonify, make_response
from flask_restful import Resource
from models.user import User
from models.comment import Comment
from models.db import db


class Comments(Resource):
    def get(self):
        users = User.objects()
        comments = []
        for user in users:
            comments.extend(user.comments)
            print(comments)
        return make_response(jsonify(user.name, comments), 200)


class NewComment(Resource):
    @jwt_required()
    def put(self):
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        if user:
            comment = Comment()
            body = request.get_json()
            comment.title = body.get("comments.title")
            comment.content = body.get("comments.content")
            user.comments.append(comment)
            user.update(**body)
            return {"message": "Updated user comments"}, 200
