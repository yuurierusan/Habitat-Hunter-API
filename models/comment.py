from datetime import datetime
from models.db import db


class Comment(db.EmbeddedDocument):
    content = db.StringField()
    title = db.StringField()
    creation_date = db.DateTimeField(default=datetime.now)
    modified_date = db.DateTimeField(default=datetime.now)
