from .db import db

class Link(db.Document):
    url = db.StringField(required=True, unique=False)
    short_url = db.StringField(required=False, unique=False)

    #Need to create a compression algorithem that compresses the site.
    def create_short_url(self):
        self.short_url = "todo"
