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
        listings = []
        users = User.objects()
        for user in users:
            listings.extend(user.listings)
        return make_response(jsonify(listings), 200)


class ListingByTitle(Resource):
    def get(self, title):
        listings = []
        users = User.objects()
        for user in users:
            listings.extend(user.listings)
            print(listings)
        for listing in listings:
            if listing.title == title:
                return make_response(jsonify(listing), 200)
        return {'msg': f'Listing `{title}` not found'}, 404


class NewListing(Resource):
    @jwt_required()
    def put(self):
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        if user:
            listing = Listing()
            body = request.get_json()
            listing.title = body.get("title")
            listing.image = body.get("image")
            listing.price = body.get("price")
            listing.content = body.get("content")
            listing.icon = body.get("icon")
            listing.amenities = body.get("amenities")
            listing.type = body.get("type")
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
                    listing.icon = request.json.get('icon', listing.icon)
                    listing.price = request.json.get('price', listing.price)
                    listing.type = request.json.get("type", listing.type)
                    listing.content = request.json.get(
                        'content', listing.content)
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
