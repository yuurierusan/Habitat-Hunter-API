from datetime import datetime
from models.db import db
import uuid


class Listing(db.EmbeddedDocument):
    id = db.StringField(primary_key=True, default=lambda: str(uuid.uuid4()))
    image = db.URLField()
    title = db.StringField()
    content = db.StringField()
    price = db.IntField()
    amenities = db.StringField()
    creation_date = db.DateTimeField(default=datetime.now)
    modified_date = db.DateTimeField(default=datetime.now)
