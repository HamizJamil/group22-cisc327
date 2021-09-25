from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
<<<<<<< HEAD
db = SQLAlchemy(app)

=======
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # ignore overhead restrictions
db = SQLAlchemy(app)

total_products = 0
list_of_products = []
>>>>>>> will_branch

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
<<<<<<< HEAD
        return '<User %r>' % self.username
=======
        return '<User %r>' % self.username


def getuniqueproductID():
    global total_products
    x = random.randint(0, list_of_products) # change this to database attributes that are passed in system
    for i in range(list_of_products):
        if x != list_of_products[i]:
            return x


class Product(db.Model):
    def __init__(self, seller):
        self.seller = seller
        self.number_of_product = int(input("Please Enter the Amount of these products you would like to sell: "))
        self.price = input("Please Enter a Price you would like to sell the product for: ")
        self.product_ID = getuniqueproductID()
        self.product_title = input("Please Enter a Product Title: ")
        self.verified_buyer = []
        self.dollars_made = 0
        self.verified_buyer_reviews = []

    def purchased(self, number_of_product, price):
        temp = self.number_of_product
        self.number_of_product -= number_of_product
        self.dollars_made = (temp-self.number_of_product)*price

    product_ID = db.Column(db.Integer, primary_key=True)
    seller = db.Column(db.String(80), primary_key=True)
    price = db.Column(db.Integer, primary_key=True)
    number_of_product = db.Column(db.Integer, primary_key=True)
    product_title = db.Column(db.String(30), primary_key=True)
    verified_buyer = db.Column(db.String(80), primary_key=True)
    dollars_made = db.Column(db.Integer, primary_key=True)
    verified_buyer_reviews = db.Column(db.String(150), primary_key=True)

    def __repr__(self):
        return '<Product: {}, {}, {}, {}, {}, {}, {}>'.format(self.product_ID, self.seller, self.price,
                                                              self.number_of_product, self.product_title,
                                                              self.verified_buyer, self.dollars_made,
                                                              self.verified_buyer_reviews)

>>>>>>> will_branch
