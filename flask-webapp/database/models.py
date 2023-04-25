from .db import db
import datetime
import hashlib


class Link(db.Document):
    # TODO Until better way to check uniqueness with seconard value, or custom short urls are added.  Keep url unique.
    url = db.StringField(required=True, unique=True)
    short_url = db.StringField(required=True, unique=True)
    isUnique = db.BooleanField(required=True, default=True)
    created = db.DateTimeField(required=False, default=datetime.datetime.now)

    def create_short_url(self, longUrl: str) -> None:
        self.short_url = self.hash_long_url(longUrl)

    def hash_long_url(self, longUrl: str):
        # TODO This should not be true, and we should't use an exception
        while True:
            m = hashlib.md5()
            m.update(longUrl.encode('ascii'))
            m.digest()
            shortUrl = m.hexdigest()[:7]
            # Check if shortUrl is in mongo db
            try:
                Link.objects.get(short_url=shortUrl)
            except Exception:
                print("url with short url was not found")
                return shortUrl
            else:
                print("Hash existed in db.")
                longUrl += "gnu"

    # def getRandomDocument(self):
    #     return db.link.aggregate([{ $sample: { size: 1 } }])

    # def addCreatedTIme(self):
    #     self.created = datetime.datetime.now()
