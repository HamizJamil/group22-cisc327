from flask import Flask
from flask_sqlalchemy import SQLAlchemy

total_products = 0
list_of_products = []

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # ignore overhead restrictions
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Product(db.Model):
    product_ID = db.Column(db.Integer, primary_key=True)
    seller = db.Column(db.String(80), primary_key=True)
    price = db.Column(db.Integer, primary_key=True)
    number_of_product = db.Column(db.Integer, primary_key=True)
    product_title = db.Column(db.String(30), primary_key=True)
    product_description = db.Column(db.String(150), primary_key=True)
    verified_buyer = db.Column(db.String(80), primary_key=True)
    dollars_made = db.Column(db.Integer, primary_key=True)
    verified_buyer_reviews = db.Column(db.String(150), primary_key=True)

    def __repr__(self):
        return '<Product: %r, %r>' % self.product_title, self.product_description
