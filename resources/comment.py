from flask import jsonify, make_response
from flask_restful import Resource
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
            comment = Comment.objects(comments=current_comment).first()
            id = Comment.objects(id=id)
            if comment and id:
                return jsonify(id), 200
            return {'msg': 'Unable to find comment'}, 404
