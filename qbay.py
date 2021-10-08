from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import date
import random
  
basedir = os.path.abspath(os.path.dirname(__file__))  
# accessing proper directory for db file
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
# ignore overhead restrictions
db = SQLAlchemy(app)
# GLOBAL VARIABLES
number_of_products = 0


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
        - product_description = the qualitative and quantitative features of 
          the product described by seller
    
    Methods:
        1. _innit__
        2. check_title_requriements
        3. check_description_requirements
        4. check_modified_date
        5. Update_Product

    """
    __tablename__ = 'Product'
    product_title = db.Column(db.String(80), primary_key=True)
    product_description = db.Column(db.String(2000), primary_key=True)
    product_ID = db.Column(db.Integer, primary_key=True)
    owner_email = db.Column(db.String(80), primary_key=True, nullable=False)
    product_price = db.Column(db.Integer, primary_key=True)
    last_date_modified = db.Column(db.String(80), primary_key=True)
    
    def __repr__(self):
        return """<Product(product_title= {}, product_description= {}, 
                product_ID= {}, owner_email= {}, price= {}, 
                last_date_modified={})>""".format(self.product_title,
                                                  self.product_description, 
                                                  self.product_ID, 
                                                  self.owner_email, 
                                                  self.product_price, 
                                                  self.last_date_modified)


def create_product(title, description, owner_email, price): 
    # method will create product as long as it follows the site instructions
    global number_of_products
    description_size = len(str(description))
    title_size = len(str(title))
    if title.startswith(' '):
        print("ERROR: No Prefixes Allowed in Title")
        return False
    if title.endswith(' '):
        print("ERROR: No Suffixes Allowed in Title")
        return False
    if not title.isalnum():
        if " " not in title:
            print("ERROR: Title MUST be Alphanumeric")
            return False
    product_exists = Product.query.filter_by(product_title=title).all()
    if len(product_exists) > 0:
        print("ERROR: Product Must Be Unique")
        return False
    if description_size < title_size:
        print("ERROR: Description Must Be Larger Than Title")
        return False
    if description_size < 20:
        print("ERROR: Description Must Be Larger Than 20 Characters")
        return False
    if price > 10000:
        print("ERROR: Price must be Less than $10000 CAD")
        return False
    if price < 10:
        print("ERROR: Price must be 1More than $10 CAD")
        return False
    user_exists = User.query.filter_by(email=owner_email)
    if user_exists == 0:
        print("ERROR: Must Have A Registered Account With QBAY")
        return False
    todays_date = date.today()  # using datetime library to access realtime val
    if todays_date.year > 2025:
        print("ERROR: Date Not Possible")
        return False
    id = number_of_products
    product = Product(product_title=title, product_description=description, 
                      product_ID=id, owner_email=owner_email,
                      product_price=price, 
                      last_date_modified=todays_date)  
    # create the product object

    db.session.add(product)
    db.session.commit()  # add product to db and save
    number_of_products += 1  # this value used to create unique ID


def update_product(search_title, new_price=None, new_title=None, 
                   new_description=None):
    global number_of_products
    # searching for product based off unique ID
    product_to_be_updated = Product.query.filter_by(product_title=search_title
                                                    ).first()
    description_size = len(str(new_description))
    title_size = len(str(new_title))
    # parameters are deafaulted to NONE so if no change is made the product 
    # is unaffected -- now evaluate the changes with our site standard
    if new_price is not None:
        if new_price < int(product_to_be_updated.product_price):
            print("ERROR: Cannot Reduce Price")
            return False
        if new_price > 10000:
            print("ERROR: Price must be Less than $10000 CAD")
            return False
        if new_price < 10:
            print("ERROR: Price must be 1More than $10 CAD")
            return False
        product_to_be_updated.product_price = new_price
    if new_title is not None:
        if new_title.startswith(' '):
            print("ERROR: No Prefixes Allowed in Title")
            return False
        if new_title.endswith(' '):
            print("ERROR: No Suffixes Allowed in Title")
            return False
        if not new_title.isalnum():
            if " "  not in new_title:
                print("ERROR: Title MUST be Alphanumeric")
                return False
        product_exists = Product.query.filter_by(product_title=new_title).all()
        if len(product_exists) > 0:
            print("ERROR: Product Must Be Unique")
            return False
        product_to_be_updated.product_title = new_title
    if new_description is not None:
        if description_size < title_size:
            print("ERROR: Description Must Be Larger Than Title")
            return False
        if description_size < 20:
            print("ERROR: Description Must Be Larger Than 20 Characters")
            return False
        product_to_be_updated.product_description = new_description
    product_to_be_updated.last_date_modified = date.today()
    # update datetime to new datetime value
    # values are only updated if user entry field is filled --> else default