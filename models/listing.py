from datetime import datetime
from models.db import db


class Listing(db.EmbeddedDocument):
    image = db.StringField()
    title = db.StringField(unique=True)
    content = db.StringField()
    price = db.IntField()
    type = db.StringField()
    icon = db.StringField()
    amenities = db.StringField()
    creation_date = db.DateTimeField(default=datetime.now)
    modified_date = db.DateTimeField(default=datetime.now)
