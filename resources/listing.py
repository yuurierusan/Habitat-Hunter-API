from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, jsonify, make_response
from flask_restful import Resource
from models.listing import Listing
from models.user import User


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
            return {"message": f"Updated {user.name} listings"}, 200
        return {"message": "Please log in"}, 404


class UpdateListing(Resource):
    @jwt_required()
    def put(self, title):
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        if user:
            for listing in user.listings:
                if listing.title == title:
                    body = request.get_json()
                    listing.image = request.json.get('image', listing.image)
                    listing.title = request.json.get('title', listing.title)
                    listing.price = request.json.get('price', listing.price)
                    listing.amenities = request.json.get(
                        'amenities', listing.amenities)
                    user.save()
                    return {"message": f"Listing `{title}` Updated"}, 200
            return {"message": f"Listing `{title}` didn't match"}, 404


class DeleteListing(Resource):
    @jwt_required()
    def delete(id, title):
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        if user:
            for listing in user.listings:
                if listing.title == title:
                    user.listings.remove(listing)
                    user.save()
                    return {"message": f"Listing `{title}` Deleted"}, 200
        return {"message": f"Listing `{title}` didn't match"}, 404
