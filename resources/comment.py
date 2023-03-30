from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, session, jsonify, make_response
from flask_restful import Resource
from models.user import User
from models.comment import Comment


def index():
    if not session.get("email"):
        return False
    return True


class Comments(Resource):
    def get(self):
        comments = Comment.objects()
        return make_response(jsonify(comments), 200)

    def get_comment_by_id(id: str):
        if index():
            comment = Comment.objects(name=current_comment).first()
            id = Comment.objects(id=id)
            if comment and id:
                return jsonify(id), 200
            return {'msg': 'Unable to find comment'}, 404


class NewComment(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        if user:
            comment = Comment()
            body = request.get_json()
            comment.title = body.get("title")
            comment.content = body.get("content")
            comment.save()
            return {"message": "Posted comment"}, 200
