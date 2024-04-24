from . import db
from flask_login import UserMixin
from sqlalchemy import func
from itsdangerous import URLSafeTimedSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from instance import config

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(150))
    vendor = db.Column(db.String(150))
    category = db.Column(db.String(150))
    item = db.Column(db.String(150))
    rating = db.Column(db.Integer)
    comments = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id  = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True)
    reviews = db.relationship('Review')
    
    def generate_token(email, password):
        serializer = Serializer(config.SECRET_KEY)
        return serializer.dumps(email, salt=password)
    
    def validate_reset_password_token(token:str, user_id:int):
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return None
        serializer = Serializer(config.SECRET_KEY)
        try:
            token_user_email = serializer.loads(token, salt=user.password)
        except (BadSignature, SignatureExpired):
            return None
        if token_user_email != user.email:
            return None
        return user
