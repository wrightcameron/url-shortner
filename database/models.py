from .db import db
from bson import ObjectId

class Link(db.Document):
    url = db.StringField(required=True, unique=False)
    short_url = db.StringField(required=True, unique=True)

    #Need to create a compression algorithem that compresses the site.
    # TODO Need a better shorter uuid, until then I can just use the unique id of the entire itself.
    def create_short_url(self):
        self.short_url = str(ObjectId())
