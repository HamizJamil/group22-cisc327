from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # ignore overhead restrictions
db = SQLAlchemy(app)


class User(db.Model):
    """
    Class to represent a user who has registered for the "ebay" site

    Attributes:
        - id = A unique ID associated to each user to validate existence of user in database
        - username = A user chosen name which is publicly seen by all other users and used to log in
        - email = An email address associated to the users' account, used to log in
        - balance = An integer amount representing the amount of currency in the users account to be spent or withdrawn
        - buyer = asserts whether or not the user is a buyer on the site
        - seller = asserts whether or not the user is a seller on the site
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    balance = db.Column(db.Integer, primary_key=True)
    buyer = db.Column(db.Boolean, primary_key=True)
    seller = db.Column(db.Boolean, primary_key=True)

    def __repr__(self):
        return "<User(id={}, username={}, email={}, balance={}, buyer={}, seller={})>".format(self.id, self.username, 
        self.email, self.balance, self.buyer, self.seller) 


class Product(db.Model):
    """
    Class to represent a product being added to "ebay" page by seller

    Attributes:
        - Product_ID = to uniquely identify a product and for easy extraction from database structure
        - Seller =  identifies what user created the product to be sold
        - Price = the amount of money the seller wishes to sell the product for
        - number_of_product = inventory of the seller for this specific product
        - product_description = the qualitative and quantitative features of the product described by seller
        - verified_buyer = list of Users who have purchased the product and has been confirmed by the system
        - dollars_made = the accumulated amount of money from this product which will be used in banking functions
        - verified_buyer_reviews = list of reviews made by confirmed verified_buyers
    """
    product_ID = db.Column(db.Integer, primary_key=True)
    seller = db.Column(db.String(80), primary_key=True)
    price = db.Column(db.Integer, primary_key=True)
    number_of_product = db.Column(db.Integer, primary_key=True)
    product_title = db.Column(db.String(30), primary_key=True)
    product_description = db.Column(db.String(150), primary_key=True)
    verified_buyer = db.Column(db.String(80), primary_key=True)
    dollars_made = db.Column(db.Integer, primary_key=True)
    verified_buyer_reviews = db.Column(db.String(150), primary_key=True)

    def __init__(self, product_ID, seller, price, number_of_product, product_title, product_description, verified_buyer,
                 dollars_made, verified_buyer_reviews):
        self.product_ID = product_ID
        self.seller = seller
        self.price = price
        self.number_of_product = number_of_product
        self.product_title = product_title
        self.product_description = product_description
        self.verified_buyer = verified_buyer
        self.dollars_made = dollars_made
        self.verified_buyer_reviews = verified_buyer_reviews

    def __repr__(self):
        return "<Product(product_title= {}, product_ID= {}, seller= {}, price= {}, number_of_product= {}, " \
               "product_description= {}, verified_buyer= {}, dollars_made= {},verified_buyer_reviews= {})>".format(
                self.product_title,self.product_ID, self.seller, self.price, self.number_of_product,
                self.product_description, self.verified_buyer, self.dollars_made, self.verified_buyer_reviews)
