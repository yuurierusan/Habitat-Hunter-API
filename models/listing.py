from datetime import datetime
from models.db import db


class Listing(db.Document):
    image_path = db.StringField()
    title = db.StringField()
    price = db.IntField()
    amenities = db.StringField()
    creation_date = db.DateTimeField(default=datetime.now)
    modified_date = db.DateTimeField(default=datetime.now)
