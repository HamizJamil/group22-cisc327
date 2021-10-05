from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))  
# accessing proper directory for db file


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
# ignore overhead restrictions
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Product(db.Model):
    """
    Class to represent a product being added to "ebay" page by seller

    Attributes:
        - Product_ID = to uniquely identify a product and for easy extraction 
          from database structure
        - owner_email =  identifies what user created the product to be sold
        - Price = the amount of money the seller wishes to sell the product for
        - number_of_product = inventory of the seller for this specific product
        - product_description = the qualitative and quantitative features of 
          the product described by seller
    """
    product_title = db.Column(db.String(30), primary_key=True)
    product_ID = db.Column(db.Integer, primary_key=True)
    owner_email = db.Column(db.String(80), primary_key=True)
    price = db.Column(db.Integer, primary_key=True)
    number_of_product = db.Column(db.Integer, primary_key=True)
    product_description = db.Column(db.String(150), primary_key=True)

    def __init__(self, product_ID, owner_email, price, number_of_product,
     product_title, product_description):
        self.product_title = product_title
        self.product_ID = product_ID
        self.owner_email = owner_email
        self.price = price
        self.number_of_product = number_of_product
        self.product_description = product_description

    def __repr__(self):
        return "<Product(product_title= {}, product_ID= {}, owner_email= {},\
            price= {}, number_of_product= {}, product_description= {})>"\
            .format(self.product_title,self.product_ID, self.owner_email, 
            self.price, self.number_of_product,  self.product_description)