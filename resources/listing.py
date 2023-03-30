from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, jsonify, make_response
from flask_restful import Resource
from models.listing import Listing


def index():
    if not session.get("email"):
        return False
    return True


class Listings(Resource):
    def get(self):
        listings = Listing.objects()
        return make_response(jsonify(listings), 200)

    def get_by_id(id: str):
        if index():
            listing = Listing.objects(title=current_listing).first()
            id = Listing.objects(id=id)
            if listing and id:
                return jsonify(id), 200
            return {'msg': 'Unable to find listing'}, 404


class NewListing(Resource):
    @jwt_required()
    def post(self):
        listing = Listing()
        body = request.get_json()
        listing.image = body.get("image")
        listing.title = body.get("title")
        listing.price = body.get("price")
        listing.amenities = body.get("amenities")
        listing.push()
        listing.save()
        return {"message": "Posted listing"}, 200


class UpdateListing(Resource):
    @jwt_required()
    def put(id):
        if index():
            current_listing = get_jwt_identity()
            listing = Listing.objects(title=current_listing).first()
            id = Listing.objects(id=id)
            if listing and id:
                body = request.get_json()
                id.update(**body)
                return jsonify(id), 200
            return {"message": "Listing id didn't match"}, 404
        return {"message": "Please log in"}, 404


class DeleteListing(Resource):
    @jwt_required()
    def delete(id):
        if index():
            current_listing = get_jwt_identity()
            listing = Listing.objects(title=current_listing).first()
            id = Listing.objects(id=id)
            if listing and id:
                id.delete()
                return jsonify(id), 200
            return {"message": "Listing id didn't match"}, 404
        return {"message": "Please log in"}, 404
