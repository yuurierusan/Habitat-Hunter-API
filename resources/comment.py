from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, jsonify, make_response
from flask_restful import Resource
from models.user import User
from models.comment import Comment


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
            comment.content = body.get("content")
            user.comments.append(comment)
            user.save()
            return {"message": "Updated user comments"}, 200
