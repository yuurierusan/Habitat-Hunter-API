from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, jsonify, make_response
from flask_restful import Resource
from models.listing import Listing
from models.user import User
from bson import ObjectId


def index():
    if not session.get("email"):
        return False
    return True


class Listings(Resource):
    def get(self):
        users = User.objects()
        listings = []
        for user in users:
            listings.extend(user.listings)
        return make_response(jsonify(listings), 200)


class ListingById(Resource):
    def get(self, id: str):
        # try:
        #     user = User.objects(id=ObjectId(id)).first()

        #     if user:
        #         return make_response(jsonify({'id': str(user.id), 'name': user.name, 'email': user.email}), 200)
        #     listing = Listing.objects(title=current_listing).first()
        #     id = Listing.objects(id=id)
        #     if listing and id:
        #         return jsonify(id), 200
        return {'msg': 'Unable to find listing'}, 404


class NewListing(Resource):
    @jwt_required()
    def put(self):
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        if user:
            listing = Listing()
            body = request.get_json()
            listing.image = body.get("image")
            listing.title = body.get("title")
            listing.price = body.get("price")
            listing.amenities = body.get("amenities")
            user.listings.append(listing)
            user.save()
            return {"message": "Updated user listings"}, 200
        return {"message": "Please log in"}, 404


class UpdateListing(Resource):
    @jwt_required()
    def put(self):
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        if user:
            listing = Listing.objects(title=listing).first()
            if listing:
                body = request.get_json()
                listing.image = body.get("image")
                listing.title = body.get("title")
                listing.price = body.get("price")
                listing.amenities = body.get("amenities")
                user.listing.update(listing)
                user.save()
                return {"message": "Listing Updated"}, 200
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
