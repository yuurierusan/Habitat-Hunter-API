from datetime import datetime
from models.db import db


class Comment(db.EmbeddedDocument):
    title = db.StringField()
    content = db.StringField()
    creation_date = db.DateTimeField(default=datetime.now)
    modified_date = db.DateTimeField(default=datetime.now)
