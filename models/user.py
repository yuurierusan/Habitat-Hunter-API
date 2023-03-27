from datetime import datetime
from models.db import db


class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    password = db.BinaryField()
    creation_date = db.DateTimeField(default=datetime.now)
    modified_date = db.DateTimeField(default=datetime.now)
