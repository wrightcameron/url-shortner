from .db import db
from bson import ObjectId

from random import choice
from string import ascii_lowercase, ascii_uppercase, digits
import datetime

class Link(db.Document):
    url = db.StringField(required=True, unique=False)
    short_url = db.StringField(required=True, unique=True)
    #created = db.DateTimeField(required=False, unique=False)

    def create_short_url(self):
        # Generate a random id, this id is a 7 character key of numbrs and upper/lowercase ascii
        # TODO This could cause conflicts, so need to a way to handle conflicts or simulate one to program handle
        self.short_url = ''.join(choice(ascii_lowercase + ascii_uppercase + digits) for i in range(7))

    # def getRandomDocument(self):
    #     return db.link.aggregate([{ $sample: { size: 1 } }])

    # def addCreatedTIme(self):
    #     self.created = datetime.datetime.now()
