from datetime import datetime
from models.db import db
import uuid


class Comment(db.EmbeddedDocument):
    id = db.StringField(primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.StringField()
    content = db.StringField()
    creation_date = db.DateTimeField(default=datetime.now)
    modified_date = db.DateTimeField(default=datetime.now)
