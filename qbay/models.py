from flask import Flask
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from qbay import app
import re  # regular expression library
# email RFC 5322 constraint

email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password_regex = re.compile(r"^(?=.{6,})(?=.*[a-z])(?=.*[A-Z])"
                            r"(?=.*[!@#$%^&+=]).*$")
postal_code_regex = re.compile(r"(^[a-zA-Z]+[0-9]+[a-zA-Z]+"
                               r"[0-9]+[a-zA-Z]+[0-9])")


app = Flask(__name__)

# Flask-WTF requires an enryption key - the string can be anything
app.config['SECRET_KEY'] = 'MC2XH243GssUWwKdTWS7FDhdwYF56wPj8'

# the name of the database; add path if necessary
db_name = 'Qbay.sqlite3'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)


# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type
class User(db.Model):
    email = db.Column(db.String(50), primary_key=True)
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
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), index=True, unique=True, nullable=False)
    description = db.Column(db.String(2000), index=True, unique=False)
    price = db.Column(db.Float, index=True, unique=False)
    last_modified_date = db.Column(db.Date, index=True, unique=False)
    owner_email = db.Column(db.String, db.ForeignKey('user.email'))
    transactions = db.relationship('Transaction', backref='product',
                                   lazy='dynamic')
    reviews = db.relationship('Review', backref='product', lazy='dynamic')

    def __init__(self, title, price, description, owner_email):
        self.title = title
        self.price = price
        self.description = description
        self.owner_email = owner_email
        self.last_modified_date = date.today()

    def __repr__(self):
        return "Product {}: {} Price: {}".format(self.id, self.title,
                                                 self.price)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, index=True, unique=False)
    date = db.Column(db.DateTime, index=True, unique=False)
    buyer = db.Column(db.String, db.ForeignKey('user.email'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __repr__(self):
        return "Transaction {}: {}, date: {}".format(self.id, self.product,
                                                     self.date)

    def __init__(self, price, buyer, product_id):
        self.price = price
        self.buyer = buyer
        self.product_id = product_id
        self.date = date.today()


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, unique=False)
    text = db.Column(db.String(200), unique=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    reviewer_user_name = db.Column(db.String, db.ForeignKey('user.user_name'))

    # get a nice printout for Review objects
    def __repr__(self):
        return "Review: {} stars: {}".format(self.text, self.stars)

    def __init__(self, stars, review_text, product_id, reviewer):
        self.stars = stars
        self.text = review_text
        self.product_id = product_id
        self.reviewer_user_name = reviewer


def register_user(user_name, user_email, user_password):
    if str(user_email) is None:
        print("ERROR: you must enter a username.")
        return False
    if str(user_password) is None:
        print("ERROR: you must enter a password.")
        return False
    email_taken = User.query.filter_by(email=user_email).all()
    if len(email_taken) != 0:
        print("ERROR: This email is already registered by an existing user." +
              " Please choose another.")
        return False
    match = re.fullmatch(email_regex, user_email)
    if not match:
        print("ERROR: Please enter a valid email address.")
        return False
    if len(str(user_password)) < 6:
        print("ERROR: Password must be longer than 6 characters.")
        return False
    if password_regex.search(user_password) is None:
        print("ERROR: Password must contain atleast one special character.")
        return False
    upper_count = 0
    for i in range(len(user_password)):
        if user_password[i].isupper():
            upper_count += 1
    if upper_count == 0:
        print("ERROR: Password does not contain captial characters.")
        return False
    lower_count = 0
    for i in range(len(user_password)):
        if user_password[i].islower():
            lower_count += 1
        if lower_count == 0:
            print("ERROR: Password does not contain lower case characters.")
            return False
    if user_name is None:
        print("ERROR: null username field.")
        return False
    if not user_name.isalnum():
        if " " not in user_name:
            print("ERROR: username MUST be Alphanumeric")
            return False
    if user_name.startswith(' '):
        print("ERROR: No Prefixes Allowed in Username")
        return False
    if user_name.endswith(' '):
        print("ERROR: No Suffixes Allowed in Username")
        return False
    if len(user_name) < 3 or len(user_name) > 19:
        print("ERROR: Username must be greater than 2 characters and less than"
              + "20.")
        return False
    user = User(email=user_email, user_name=user_name, password=user_password)
    db.session.add(user)
    db.session.commit()
    return True


def login(email, password):
    if email is None:
        print("ERROR: you must enter a username.")
        return None
    if password is None:
        print("ERROR: you must enter a password.")
        return None
    if len(password) < 6:
        print("ERROR: Incorrect password length.")
        return None
    if password_regex.search(password) is None:
        print("ERROR: No Special Characters.")
        return None
    upper_count = 0
    for i in range(len(password)):
        if password[i].isupper():
            upper_count += 1
    if upper_count == 0:
        print("ERROR: Password does not contain captial characters.")
        return None
    lower_count = 0
    for i in range(len(password)):
        if password[i].islower():
            lower_count += 1
        if lower_count == 0:
            print("ERROR: Password does not contain lower case characters.")
            return None
    match = re.fullmatch(email_regex, email)
    if not match:
        print("Incorrect email format.")
        return None
    retrieved_user = User.query.filter_by(email=email,
                                          password=password).all()
    if len(retrieved_user) != 1:
        return None
    return retrieved_user[0]


def update_user(search_email, new_username=None, shipping_address=None,
                postal_code=None):
    # account is already logged in so system will grab email from current
    # account logged in

    # Since account must already be valid/real to be logged in no need to
    # revalidate on user end
    user_to_be_updated = User.query.filter_by(email=search_email)
    if user_to_be_updated is None:
        print("SYSTEM ERROR: Account cannot updated - account not linked")
        return None
    if new_username is not None:
        if new_username == "":  # empty username field
            print("ERROR: New Username cannot be empty")
            return None
        for char in new_username:
            if char.isalnum() is False and char != " ":
                print("ERROR: Username must be all alphanumeric")
                return None
        if new_username[0] == " ":
            print("ERROR: No space as the prefix in new username")
            return None
        if new_username[len(new_username) - 1] == " ":
            print("ERROR: No spaces as suffix in new user name")
            return None
    user_to_be_updated.user_name = new_username
    if shipping_address is None:
        print("ERROR: Shipping Address cannot be empty")
        return None
    for char in shipping_address:
        if char.isalnum() is False and char != " ":
            print("ERROR: Shipping Address must be all alphanumeric")
            return None
        if password_regex.search(char) is None:
            print("ERROR: No Special Characters")
    user_to_be_updated.shipping_address = shipping_address
    match = re.fullmatch(postal_code_regex, postal_code)
    if not match:
        print("ERROR: Please enter a valid postal code")
    user_to_be_updated.postal_code = postal_code
    return user_to_be_updated


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
    product_exists = Product.query.filter_by(title=title).all()
    if len(product_exists) > 0:
        print("ERROR: Product Must Be Unique")
        return False
    if int(description_size) < int(title_size):
        print("ERROR: Description Must Be Larger Than Title")
        return False
    if int(description_size) < 20:
        print("ERROR: Description Must Be Larger Than 20 Characters")
        return False
    if int(price) > 10000:
        print("ERROR: Price must be Less than $10000 CAD")
        return False
    if int(price) < 10:
        print("ERROR: Price must be 1More than $10 CAD")
        return False
    user_exists = User.query.filter_by(email=owner_email).first()
    if user_exists == 0:
        print("ERROR: Must Have A Registered Account With QBAY")
        return False
    product = Product(title=title, price=price,
                      description=description,
                      owner_email=owner_email)
    # create the product object
    db.session.add(product)
    db.session.commit()  # add product to db and save
    return True


def update_product(search_title, owner_email, new_price=None, new_title=None,
                   new_description=None):
    global number_of_products
    # searching for product based off unique ID
    product_to_be_updated = Product.query.filter_by(title=search_title,
                                                    owner_email=owner_email
                                                    ).first()
    description_size = len(str(new_description))
    title_size = len(str(new_title))
    # parameters are deafaulted to NONE so if no change is made the product
    # is unaffected -- now evaluate the changes with our site standard
    if product_to_be_updated is None:
        print("No product by that search filter")
        return None
    if new_price is not None:
        if int(new_price) < int(product_to_be_updated.price):
            print("ERROR: Cannot Reduce Price")
            return None
        if int(new_price) > 10000:
            print("ERROR: Price must be Less than $10000 CAD")
            return None
        if int(new_price) < 10:
            print("ERROR: Price must be 1More than $10 CAD")
            return None
        product_to_be_updated.price = new_price
    if new_title is not None:
        if new_title.startswith(' '):
            print("ERROR: No Prefixes Allowed in Title")
            return None
        if new_title.endswith(' '):
            print("ERROR: No Suffixes Allowed in Title")
            return None
        if not new_title.isalnum():
            if " " not in new_title:
                print("ERROR: Title MUST be Alphanumeric")
                return None
        product_exists = Product.query.filter_by(title=new_title).all()
        if len(product_exists) > 0:
            print("ERROR: Product Must Be Unique")
            return None
        product_to_be_updated.title = new_title
    if new_description is not None:
        if description_size < title_size:
            print("ERROR: Description Must Be Larger Than Title")
            return None
        if description_size < 20:
            print("ERROR: Description Must Be Larger Than 20 Characters")
            return None
        product_to_be_updated.product_description = new_description
    product_to_be_updated.last_date_modified = date.today()
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
    buyer_email = User.query.filter_by(email=email).first()
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
