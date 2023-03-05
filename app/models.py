from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), index = True, unique = True)
    email = db.Column(db.String(60), index = True, unique = True)
    password_hash = db.Column(db.String(120))
    admin = db.Column(db.Boolean, index = True, default=False)
    
    def __repr__(self) -> str:
        return '<User {}'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Goods(db.Model):
    __tablename__ = 'Goods'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(45), index = True, unique=True)
    descreption = db.Column(db.String(420), index = True)
    price = db.Column(db.Integer, index = True)
    size = db.Column(db.String(50), index = True)
    matherial = db.Column(db.String(75), index = True)
    type = db.Column(db.String(80), index = True)
    quantity = db.Column(db.Integer, index = True)
    in_stock = db.Column(db.String, default=True, index = True)
    image_name = db.Column(db.String, index = True)
    publish_date = db.Column(db.DateTime, default=datetime.now(), index = True)
    
    def __repr__(self) -> str:
        return f'name: {self.name}, price: {self.price}'
