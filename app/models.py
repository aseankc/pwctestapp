from app import db
import json

class ComData(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    cname = db.Column (db.String (80), nullable = False)
    description = db.Column (db.String (80), nullable = False)
    tagline = db.Column (db.String (80), nullable = False)
    email = db.Column (db.String (80), nullable = False)
    businessnumber = db.Column (db.Integer, nullable = False)
    restricted = db.Column (db.String (80), nullable = False)

    def serialize (self):
        return {
            'id': self.id,
            'name': self.cname,
            'description': self.description,
            'email': self.email,
            'businessnumber': self.businessnumber,
            'restricted': self.restricted
        }