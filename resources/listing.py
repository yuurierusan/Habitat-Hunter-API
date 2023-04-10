from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, jsonify, make_response
from flask_restful import Resource
from models.listing import Listing
from models.user import User


class Listings(Resource):
    def get(self):
        listings = []
        users = User.objects()
        for user in users:
            listings.extend(user.listings)
            print(user.listings)
        return make_response(listings)
        # return {'msg': 'No listings found'}, 404


class ListingById(Resource):
    def get(self, id):
        listings = []
        users = User.objects()
        for user in users:
            listings.extend(user.listings)
            print(listings)
        for listing in listings:
            if listing.id == id:
                return make_response(jsonify(listing), 200)
        return {'msg': f'Listing `{id}` not found'}, 404


class NewListing(Resource):
    @jwt_required()
    def put(self):
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        print(user, 'We hit the new listing route')
        if user:
            listing = Listing()
            body = request.get_json()
            listing.title = body.get("title")
            listing.image = body.get("image")
            listing.price = body.get("price")
            listing.content = body.get("content")
            listing.amenities = body.get("amenities")
            user.listings.append(listing)
            user.save()
            return {"message": f"Updated {user.name} listings"}, 200
        return {"message": "Please log in"}, 404


class UpdateListing(Resource):
    @jwt_required()
    def put(self, id):
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        if user:
            for listing in user.listings:
                if listing.id == id:
                    body = request.get_json()
                    listing.image = request.json.get('image', listing.image)
                    listing.title = request.json.get('title', listing.title)
                    listing.price = request.json.get('price', listing.price)
                    listing.content = request.json.get(
                        'content', listing.content)
                    listing.amenities = request.json.get(
                        'amenities', listing.amenities)
                    user.save()
                    return {"message": f"Listing `{id}` Updated"}, 200
            return {"message": f"Listing `{id}` didn't match"}, 404


class DeleteListing(Resource):
    @jwt_required()
    def delete(self, id):
        current_user = get_jwt_identity()
        user = User.objects(email=current_user).first()
        if user:
            for listing in user.listings:
                if listing.id == id:
                    user.listings.remove(listing)
                    user.save()
                    return {"message": f"Listing `{id}` Deleted"}, 200
        return {"message": f"Listing `{id}` didn't match"}, 404
