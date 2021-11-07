from flask import Flask, redirect, url_for, render_template
from flask import request, session, flash
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import flag_modified
from qbay import app
import re  # regular expression library
# Different regex's to quickly search inputs and compare with constraints
email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password_regex = re.compile(r"^(?=.{6,})(?=.*[a-z])(?=.*[A-Z])" +
                            r"(?=.*[!@#$%^&+=]).*$")
shipping_regex = re.compile(r"^[A-Za-z0-9,. ';/_-]+$")
postal_regex = re.compile(r"[A-Za-z][0-9][A-Za-z] ?[0-9][A-Za-z][0-9]$")

db = SQLAlchemy(app)


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
    email = db.Column(db.String(50), primary_key=True, unique=True)
    user_name = db.Column(db.String(20), index=True, unique=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    shipping_address = db.Column(db.String(100), index=True, unique=False)
    postal_code = db.Column(db.String(7), index=True, unique=False)
    balance = db.Column(db.Integer, index=True, unique=False)
    # relationship between User and other Models
    products = db.relationship('Product', backref='user', lazy='dynamic')
    reviews = db.relationship('Review', backref='user', lazy='dynamic')
    transactions = db.relationship('Transaction', backref='user',
                                   lazy='dynamic')

    def __init__(self, email, user_name, password, shipping=None,
                 post=None, balance=100):
        self.email = email
        self.user_name = user_name
        self.password = password
        self.shipping_address = shipping
        self.postal_code = post
        self.balance = balance

    def __repr__(self):
        return "User: {} {}".format(self.user_name, self.email)


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
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), index=True, unique=True, nullable=False)
    description = db.Column(db.String(2000), index=True, unique=False)
    price = db.Column(db.Float, index=True, unique=False)
    owner_email = db.Column(db.String, db.ForeignKey('user.email'))
    last_date_modified = db.Column(db.String(20), index=True, unique=False)

    def __init__(self, title, price, description, owner_email,
                 today=str(date.today())):
        self.title = title
        self.price = price
        self.description = description
        self.owner_email = owner_email
        self.last_date_modified = today

    def __repr__(self):
        return "Product {}: {} Price: {}".format(self.id, self.title,
                                                 self.price)


class Transaction(db.Model):
    """
    Class to represent each transaction

    Attributes:
    - id - incremental
    - user_email
    - product_id
    - price
    - date
    """
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, index=True, unique=False)
    buyer = db.Column(db.String, db.ForeignKey('user.email'))

    def __repr__(self):
        return "Transaction {}: {}, date: {}".format(self.id, self.product,
                                                     self.date)

    def __init__(self, price, buyer_email):
        self.price = price
        self.buyer_email = buyer_email


class Review(db.Model):
    """
    Class to represent a product review

    Attributes:
        - id - to identify the review in the system and to be easily queried
        - user_email - identifies the owner that created the review
        - score - a score out of 10, 10 being great, 0 being awful
        - review - body of text that supports the overall score
    """
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, unique=False)
    text = db.Column(db.String(200), unique=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    reviewer_user_name = db.Column(db.String, db.ForeignKey('user.user_name'))

    # get a nice printout for Review objects
    def __repr__(self):
        return "Review: {} stars: {}".format(self.text, self.stars)

    def __init__(self, stars, text):
        self.stars = stars
        self.text = text


# function to send errors to frontend

def error_handler(message):
    flash(message)


def register_user(user_name, user_email, user_password, erro_handler=None):
    if str(user_email) is None:
        if erro_handler is not None:
            error_handler("ERROR: you must enter a username.")
        return False
    if str(user_password) is None:
        if erro_handler is not None:
            error_handler("ERROR: you must enter a password.")
        return False
    email_taken = User.query.filter_by(email=user_email).first()
    if email_taken is not None:
        if erro_handler is not None:
            error_handler("ERROR: This email is already registered by" +
                          "an existing user. Please choose another.")
        return False
    match = re.fullmatch(email_regex, user_email)
    if not match:
        if erro_handler is not None:
            error_handler("ERROR: Please enter a valid email address.")
        return False
    if len(str(user_password)) < 6:
        if erro_handler is not None:
            error_handler("ERROR: Password must be longer than 6 characters.")
        return False
    if password_regex.search(user_password) is None:
        if erro_handler is not None:
            error_handler("ERROR: Password must contain at least one" +
                          "special character.")
        return False
    upper_count = 0
    for i in range(len(user_password)):
        if user_password[i].isupper():
            upper_count += 1
    if upper_count == 0:
        if erro_handler is not None:
            error_handler("ERROR: Password does not contain" +
                          " captial characters.")
        return False
    lower_count = 0
    for i in range(len(user_password)):
        if user_password[i].islower():
            lower_count += 1
    if lower_count == 0:
        if erro_handler is not None:
            error_handler("ERROR: Password does not contain lower" +
                          "case characters.")
        return False
    if user_name is None:
        if erro_handler is not None:
            error_handler("ERROR: null username field.")
        return False
    if not user_name.isalnum():
        if " " in user_name:
            if erro_handler is not None:
                error_handler("ERROR: username MUST be Alphanumeric")
            return False
    if user_name.startswith(' '):
        if erro_handler is not None:
            error_handler("ERROR: No Prefixes Allowed in Username")
        return False
    if user_name.endswith(' '):
        if erro_handler is not None:
            error_handler("ERROR: No Suffixes Allowed in Username")
        return False
    if len(user_name) < 3 or len(user_name) > 19:
        if erro_handler is not None:
            error_handler("ERROR: Username must be greater than 2"
                          + " characters and less than 20.")
        return False
    user = User(email=user_email, user_name=user_name, password=user_password)
    db.session.add(user)
    db.session.commit()
    return True


def login(email, password, erro_handler=None):
    if email is None:
        if erro_handler is not None:
            error_handler("ERROR: you must enter an email.")
        return None
    if password is None:
        if erro_handler is not None:
            error_handler("ERROR: you must enter a password.")
        return None
    if len(password) < 6:
        if erro_handler is not None:
            error_handler("ERROR: Incorrect password length.")
        return None
    if password_regex.search(password) is None:
        if erro_handler is not None:
            error_handler("ERROR: No Special Characters.")
        return None
    upper_count = 0
    for i in range(len(password)):
        if password[i].isupper():
            upper_count += 1
    if upper_count == 0:
        if erro_handler is not None:
            error_handler("ERROR: Password does not" +
                          " contain captial characters.")
        return None
    lower_count = 0
    for i in range(len(password)):
        if password[i].islower():
            lower_count += 1
    if lower_count == 0:
        if erro_handler is not None:
            error_handler("ERROR: Password does not contain" +
                          " lower case characters.")
        return None
    match = re.fullmatch(email_regex, email)
    if not match:
        if erro_handler is not None:
            error_handler("Incorrect email format.")
        return None
    retrieved_user = User.query.filter_by(email=email,
                                          password=password).all()
    if len(retrieved_user) != 1:
        return None
    return retrieved_user[0]


def update_user(search_email, new_username=None, shipping_address=None,
                postal_code=None, erro_handler=None):
    # account is already logged in so system will grab email from current
    # account logged in

    # Since account must already be valid/real to be logged in no need to
    # revalidate on user end
    user_to_be_updated = User.query.filter_by(email=search_email).first()
    if user_to_be_updated is None:
        if erro_handler is not None:
            error_handler("SYSTEM ERROR: Account cannot updated" +
                          " - account not linked")
        return None
    if new_username is not None:
        if len(new_username) <= 2:
            if erro_handler is not None:
                error_handler("ERROR: New Username has to be "
                              "longer than 2 characters")
            return None
        if len(new_username) > 20:
            if erro_handler is not None:
                error_handler("ERROR: New Username can't be longer than 20"
                              "characters")
            return None
        if new_username == "":  # empty username field
            if erro_handler is not None:
                error_handler("ERROR: New Username cannot be empty")
            return None
        for char in new_username:
            if char.isalnum() is False and char != " ":
                if erro_handler is not None:
                    error_handler("ERROR: Username must be all alphanumeric")
                return None
        if new_username[0] == " ":
            if erro_handler is not None:
                error_handler("ERROR: No space as the prefix in new username")
            return None
        if new_username[len(new_username) - 1] == " ":
            if erro_handler is not None:
                error_handler("ERROR: No spaces as suffix in new user name")
            return None
    user_to_be_updated.user_name = new_username
    if shipping_address is None:
        if erro_handler is not None:
            error_handler("ERROR: Shipping Address cannot be empty")
        return None
    shipping_match = re.fullmatch(shipping_regex, shipping_address)
    if not shipping_match:
        if erro_handler is not None:
            error_handler("ERROR: Shipping address has to be alphanumeric")
        return None
    user_to_be_updated.shipping_address = shipping_address
    postal_match = re.fullmatch(postal_regex, postal_code)
    if not postal_match:
        if erro_handler is not None:
            error_handler("ERROR: Please enter a valid postal code")
        return None
    user_to_be_updated.postal_code = postal_code.upper().replace(" ", "")
    db.session.commit()
    return user_to_be_updated


def create_product(title, description, owner_email, price, erro_handler=None):
    # method will create product as long as it follows the site instructions
    global number_of_products
    description_size = len(str(description))
    title_size = len(str(title))
    count = 0
    current_user = User.query.filter_by(email=owner_email).first()
    if current_user is None:
        if erro_handler is not None:
            error_handler("ERROR: No user found")
        count += 1
        return False
    if title.startswith(' '):
        if erro_handler is not None:
            error_handler("ERROR: No Prefixes Allowed in Title")
        count += 1
        return False
    if title.endswith(' '):
        if erro_handler is not None:
            error_handler("ERROR: No Suffixes Allowed in Title")
        count += 1
        return False
    if not title.isalnum():
        if " " not in title:
            if erro_handler is not None:
                error_handler("ERROR: Title MUST be Alphanumeric")
            count += 1
            return False
    product_exists = Product.query.filter_by(title=title).all()
    if len(product_exists) > 0:
        if erro_handler is not None:
            error_handler("ERROR: Product Must Be Unique")
        count += 1
        return False
    if int(description_size) < int(title_size):
        if erro_handler is not None:
            error_handler("ERROR: Description Must Be Larger Than Title")
        count += 1
        return False
    if int(description_size) > 2000:
        if erro_handler is not None:
            error_handler("ERROR: Description Must Be Smaller" +
                          " Than 2000 Characters")
        count += 1
        return False
    if int(description_size) < 20:
        if erro_handler is not None:
            error_handler("ERROR: Description Must Be Larger" +
                          " Than 20 Characters")
        count += 1
        return False
    if int(price) > 10000:
        if erro_handler is not None:
            error_handler("ERROR: Price must be Less than $10000 CAD")
        count += 1
        return False
    if int(price) < 10:
        if erro_handler is not None:
            error_handler("ERROR: Price must be More than $10 CAD")
        count += 1
        return False
    user_exists = User.query.filter_by(email=owner_email).first()
    if user_exists == 0:
        if erro_handler is not None:
            error_handler("ERROR: Must Have A Registered Account With QBAY")
        count += 1
        return False
    # if count == 0:

    product = Product(title=title, price=price,
                      description=description,
                      owner_email=owner_email)
    # create the product object
    db.session.add(product)
    db.session.commit()  # add product to db and save
    return True


def update_product(search_title, owner_email, new_price=None, new_title=None,
                   new_description=None, erro_handler=None):
    global number_of_products
    # searching for product based off unique ID
    product_to_be_updated = Product.query.filter_by(title=search_title,
                                                    owner_email=owner_email)\
        .first()
    description_size = len(str(new_description))
    title_size = len(str(new_title))
    # parameters are deafaulted to NONE so if no change is made the product
    # is unaffected -- now evaluate the changes with our site standard
    if product_to_be_updated is None:
        if erro_handler is not None:
            error_handler("No product by that search filter")
        return None
    if new_price is not None:
        if int(new_price) < int(product_to_be_updated.price):
            if erro_handler is not None:
                error_handler("ERROR: Cannot Reduce Price")
            return None
        if int(new_price) > 10000:
            if erro_handler is not None:
                error_handler("ERROR: Price must be Less than $10000 CAD")
            return None
        if int(new_price) < 10:
            if erro_handler is not None:
                error_handler("ERROR: Price must be 1More than $10 CAD")
            return None
        product_to_be_updated.price = new_price
    if new_title is not None:
        if new_title.startswith(' '):
            if erro_handler is not None:
                error_handler("ERROR: No Prefixes Allowed in Title")
            return None
        if new_title.endswith(' '):
            if erro_handler is not None:
                error_handler("ERROR: No Suffixes Allowed in Title")
            return None
        if not new_title.isalnum():
            if " " not in new_title:
                if erro_handler is not None:
                    error_handler("ERROR: Title MUST be Alphanumeric")
                return None
        product_exists = Product.query.filter_by(title=new_title).all()
        if len(product_exists) > 0:
            if erro_handler is not None:
                error_handler("ERROR: Product Must Be Unique")
            return None
        product_to_be_updated.title = new_title
    if new_description is not None:
        if description_size < title_size:
            if erro_handler is not None:
                error_handler("ERROR: Description Must Be Larger Than Title")
            return None
        if description_size < 20:
            if erro_handler is not None:
                error_handler("ERROR: Description Must Be Larger" +
                              " Than 20 Characters")
            return None
        product_to_be_updated.description = new_description
    product_to_be_updated.last_date_modified = date.today()
    db.session.commit()
    return product_to_be_updated


def create_review(email, score, review):
    global number_of_reviews
    review_creator = User.query.filter_by(email=email)
    if review_creator is None:
        print("ERROR: account not registered please make an account")
        return False
    if type(score) is not int:
        print("ERROR: Score must be an integer")
        return False
    if review == "" or review == " ":
        print("Review must have text describing rating")
        return False
    if len(review) > 150:
        print("ERROR: Review must be at most 150 characters")
        return False
    review = Review(stars=score, text=review)
    # create the product object
    db.session.add(review)
    db.session.commit()  # add product to db and save
    return True


def create_transaction(email, price):
    global number_of_transactions
    buyer_email = User.query.filter_by(email=email)
    if buyer_email is None:
        print("ERROR: Account Not registered please create an account")
        return False
    price_search = Product.query.filter_by(price=price)
    if price_search is None:
        print("ERROR: Account Not registered please create an account")
        return False
    transaction = Transaction(buyer_email=email, price=price)
    # create the product object
    db.session.add(transaction)
    db.session.commit()  # add product to db and save
    return True


db.create_all()
