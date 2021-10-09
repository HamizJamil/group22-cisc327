from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import date
import random
from email.utils import parseaddr
import re
  
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
number_of_reviews = 0
special_characters = "!@#$%^&*()-+?_=,<>/"
email_regex = r'/^(?!(?>(?1)"?(?>\\\[ -~]|[^"])"?(?1)){255,})\
            (?!(?>(?1)"?(?>\\\[ -~]|[^"])"?(?1)){65,}@)((?\
            >(?>(?>((?>(?>(?>\x0D\x0A)?[\t ])+|(?>[\t ]*\
            \x0D\x0A)?[\t ]+)?)(\((?>(?2)(?>[\x01-\x08\x0B\x0C\x0E\
            -\'*-\[\]-\x7F]|\\\[\x00-\x7F]|(?3)))*(?2)\)))+(?2))|(?2))\
            ?)([!#-\'*+\/-9=?^-~-]+|"(?>(?2)(?>[\x01-\x08\x0B\x0C\x0E\
            -!#-\[\]-\x7F]|\\\[\x00-\x7F]))*(?2)")(?>(?1)\.(?1)(?4))*(?1)\
            @(?!(?1)[a-z\d-]{64,})(?1)(?>([a-z\d](?>[a-z\d-]*[a-z\d])?)(?>\
            (?1)\.(?!(?1)[a-z\d-]{64,})(?1)(?5)){0,126}|\[(?:(?>IPv6:(?>(\
            [a-f\d]{1,4})(?>:(?6)){7}|(?!(?:.*[a-f\d][:\]]){8,})((?6)(?>:\
            (?6)){0,6})?::(?7)?))|(?>(?>IPv6:(?>(?6)(?>:(?6)){5}:|(?!(?:.*\
            [a-f\d]:){6,})(?8)?::(?>((?6)(?>:(?6)){0,4}):)?))?(25[0-5]|\
            2[0-4]\d|1\d{2}|[1-9]?\d)(?>\.(?9)){3}))\])(?1)$/isD'\



class User(db.Model):
    """
    Class to represent a user who has registered for the "ebay" site

    Attributes:
        - email = An email address associated to the users' account, 
          used to log in and identify the user
        - username = A user chosen name which is associated with the
          users account, maximum 20 characters long
        - password = A password associated to the users account, used
          in conjunction with email to log in
        - shipping_address = Shipping address for the user, can be left
          empty upon registration
        - postal_code = Postal code associated with users' address, can
          be left empty upon registration
        - balance = An integer amount representing the amount of currency
          in the users account to be spent or withdrawn
    """
    __tablename__ = 'User'
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(120), primary_key=True)
    shipping_address = db.Column(db.String(120), nullable=True)
    postal_code = db.Column(db.String(20), nullable=True)
    balance = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return """<User(email= {}, user_name= {}, password= {},
                shipping_address= {}, postal_code= {},
                balance= {})>""".format(self.email,
                                        self.user_name, 
                                        self.password, 
                                        self.shipping_address, 
                                        self.postal_code, 
                                        self.balance)


def register_user(user,user_email,user_password):
    if user_email is None:
        print("ERROR: you must enter a username.")
        return False
    if user_password is None: 
        print("ERROR: you must enter a password.")
        return False
    user_taken = User.query.filter_by(email=user_email).all()
    if user_taken > 0:
        print("This username is taken by an existing user. Please choose another.")
        return False
    match = re.fullmatch(email_regex, user_email)
    if not match:
        print("ERROR: Please enter a valid email address.")
        return False
    if len(user_password)<6:
                print("ERROR: Password must be longer than 6 characters.")
                return False
    if not any(c in special_characters for c in user_password):
                print("ERROR: Password must contain atleast one special character.")
                return False
    for char in user_password:
        i= char.isupper()
        if i ==True:
            break
    if i is not True:
        print("ERROR: Password must contain atleast one upper case letter.")
        return False
    for char in user_password:
        i= char.islower()
        if i ==True:
            break
    if i is not True:
                print("ERROR: Password must contain atleast one lower case letter.")
                return False
    if user is None:
                print("ERROR: null username field.")
                return False
    if not user.isalnum():
                print("ERROR: username MUST be Alphanumeric")
                return False
    if user.startswith(' '):
                print("ERROR: No Prefixes Allowed in Username")
                return False
    if user.endswith(' '):
        print("ERROR: No Suffixes Allowed in Username")
        return False
    if len(user) < 3 or len(user) > 19:
        print("ERROR: Username must be greater than 2 characters and less than 20.")
        return False
    user = User(username=user,email=user_email,password=user_password,
                shipping_address=None, postal_code=None, balance=100)
    db.session.add(user)
    db.session.commit()


def login(email, password):
    if email is None:
        print("ERROR: you must enter a username.")
        return False
    if password is None: 
        print("ERROR: you must enter a password.")
        return False
    if len(password) < 6:
        print("ERROR: Incorrect password.")
        return False
    if not any(c in special_characters for c in password):
        print("ERROR: Incorrect password.")
        return False
    for char in password:
        i = char.isupper()
        if i is True:
            break
        if i is not True:
            print("ERROR: Incorrect password.")
            return False
    for char in password:
        i = char.islower()
        if i is True:
            break
        if i is not True:
            print("ERROR: Incorrect password.")
            return False
    match = re.fullmatch(email_regex, email)
    if not match:
        print("Incorrect email.")
        return False
    retrieved_user = db.query(User).filter(User.email == email, 
                                           User.password == password)
    return retrieved_user.first()
        

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


def update_product(title, new_price=None, new_title=None, 
                   new_description=None):
    global number_of_products
    # searching for product based off unique ID
    product_to_be_updated = Product.query.filter_by(product_title=title
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


class review(db.Model):
    """
    Class to represent a product review

    Attributes:
        - review_ID = to uniquely identify a review and for easy extraction 
          from database structure
        - user_email =  identifies what user created the review
        - review = a string containing the customers product review
        - review_time = the time at which the review was submitted 
        -score = rating given to the product by the reviewer
        -product_ID = the product ID of the product being reviewed
    """

    review_ID = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(80),nullable=False)
    score = db.Column(db.Integer,nullable=False)
    review = db.Column(db.String(400),nullable=True)
    review_time = db.Column(db.String(80))
    product_ID = db.Column(db.Integer,nullable=False)

    
# class transaction(db.Model, User, Product):
#     """
#     Class to represent each transaction 

#     Attributes:
#         - transaction_id = to uniquely identify a transaction and for easy extraction 
#           from database structure
#         - user_email =  identifies what user bought the product
#         -product_ID = the product ID of the product that was sold
#         -price = the price the product was sold for
#     """

#     transaction_id = db.Column(db.Integer, primary_key=True)
#     user_email = db.Column(db.String(80),primary_key=True)
#     product_ID = db.Column(db.Integer,primary_key=True)
#     price = db.Column(db.Integer,primary_key=True)