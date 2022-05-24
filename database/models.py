from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Link(db.Document):
    url = db.StringField(required=True, unique=True)
    short_url = db.StringField(required=True, unique=True)

    #Need to create a compression algorithem that compresses the site.
    def create_short_url(self):
        self.short_url = "todo"

# class User(db.Document):
#    email = db.EmailField(required=True, unique=True)
#    password = db.StringField(required=True, min_length=6)
#    movies = db.ListField(db.ReferenceField('Movie', reverse_delete_rule=db.PULL))
#
#    def hash_password(self):
#        self.password = generate_password_hash(self.password).decode('utf8')
#
#    def check_password(self, password):
#        return check_password_hash(self.password, password)
#
#User.register_delete_rule(Movie, 'added_by', db.CASCADE)
