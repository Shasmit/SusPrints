from enum import unique
from __init__ import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

class user(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    number = db.Column(db.String(10), nullable=True, unique=True)
    address = db.Column(db.String(120), nullable=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class MostSelling(db.Model):
    __tablename__ = "mostselling"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(500),nullable=False)
    image = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    productType = db.Column(db.String(50), nullable=False)
    discount = db.Column(db.Integer)
    def __repr__(self):
        return f"MostSelling('{self.title}', '{self.description}', '{self.image}', '{self.price}', '{self.productType}', '{self.discount}')"
        
class NewArrivals(db.Model):
    __tablename__ = "newarrivals"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),  nullable=False)
    description = db.Column(db.String(500),  nullable=False)
    image = db.Column(db.String(500),  nullable=False)
    price = db.Column(db.Integer,  nullable=False)
    productType = db.Column(db.String(50),  nullable=False)
    def __repr__(self):
        return f"NewArrivals('{self.title}', '{self.description}', '{self.image}', '{self.price}', '{self.productType}')"

class AddCart(db.Model):
    __tablename__ = "addcart"
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50), nullable=False)


    def __repr__(self):
        return f"AddCart('{self.item_id}')"