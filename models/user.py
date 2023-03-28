from datetime import datetime
from models.db import db
from models.comment import Comment
from models.listing import Listing


class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    password = db.BinaryField()
    comments = db.EmbeddedDocumentListField(Comment)
    listings = db.EmbeddedDocumentListField(Listing)
    creation_date = db.DateTimeField(default=datetime.now)
    modified_date = db.DateTimeField(default=datetime.now)
