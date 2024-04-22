from . import db
from flask_login import UserMixin
from sqlalchemy import func

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(150))
    vendor_name = db.Column(db.String(150))
    item = db.Column(db.String(150))
    rating = db.Column(db.Float)
    comments = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id  = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True)
    notes = db.relationship('Review')