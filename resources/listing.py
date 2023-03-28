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

    def get_listing_by_id(id: str):
        if index():
            listing = Listing.objects(listing=current_listing).first()
            id = Listing.objects(id=id)
            if listing and id:
                return jsonify(id), 200
            return {'msg': 'Unable to find listing'}, 404

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
