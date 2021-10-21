from qbay import app
from flask_sqlalchemy import SQLAlchemy
import re
from datetime import date


db = SQLAlchemy(app)
# GLOBAL VARIABLES
number_of_products = 0
number_of_reviews = 0
number_of_transactions = 0
special_characters = "!@#$%^&*()-+?_=,<>/"
email_regex = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|ca|net)"
postal_regex = r"[A-Za-z][0-9][A-Za-z] [0-9][A-Za-z][0-9]"


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
    user_name = db.Column(db.String(20), primary_key=True, nullable=False)
    user_email = db.Column(db.String(80), primary_key=True, nullable=False)
    user_password = db.Column(db.String(100), primary_key=True, nullable=False)
    shipping_address = db.Column(db.String(80), default="", nullable=True,
                                 primary_key=True)
    postal_code = db.Column(db.String(6), default="", nullable=True,
                            primary_key=True)
    balance = db.Column(db.Integer, default=100, primary_key=True)

    def __repr__(self):
        return """<User(user_email= {}, user_name= {}, user_password= {},
                shipping_address= {}, postal_code= {},
                balance= {})>""".format(self.user_email,
                                        self.user_name, 
                                        self.user_password, 
                                        self.shipping_address, 
                                        self.postal_code, 
                                        self.balance)


def register_user(user_name, user_email, user_password):
    if str(user_email) is None:
        print("ERROR: you must enter a username.")
        return False
    if str(user_password) is None: 
        print("ERROR: you must enter a password.")
        return False
    email_taken = User.query.filter_by(user_email=user_email).all()
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
    if not any(c in special_characters for c in user_password):
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
            print("ERROR: Password does not contail lower case characters.")
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
    user = User(user_name=user_name, user_email=user_email,
                user_password=user_password, balance=100)
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
    if not any(c in special_characters for c in password):
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
    retrieved_user = User.query.filter_by(user_email=email,
                                          user_password=password).all()
    if len(retrieved_user) != 1:
        return None
    return retrieved_user[0]


def update_user(search_email, new_username=None, shipping_address=None,
                postal_code=None):
    # account is already logged in so system will grab email from current 
    # account logged in

    # Since account must already be valid/real to be logged in no need to 
    # revalidate on user end
    user_to_be_updated = User.query.filter_by(user_email=search_email)
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
        for i in special_characters:
            if char == i:
                print("ERROR: No Special Characters")
    user_to_be_updated.shipping_address = shipping_address
    match = re.fullmatch(postal_regex, postal_code)
    if not match:
        print("ERROR: Please enter a valid postal code")
    user_to_be_updated.postal_code = postal_code
    return user_to_be_updated


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
    owner_email = db.Column(db.String(80), db.ForeignKey('User.user_email'), 
                            nullable=False)
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
    user_exists = User.query.filter_by(user_email=owner_email).first()
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
    return True


def update_product(search_title, owner_email, new_price=None, new_title=None, 
                   new_description=None):
    global number_of_products
    # searching for product based off unique ID
    product_to_be_updated = Product.query.filter_by(product_title=search_title, 
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
        if new_price < int(product_to_be_updated.product_price):
            print("ERROR: Cannot Reduce Price")
            return None
        if new_price > 10000:
            print("ERROR: Price must be Less than $10000 CAD")
            return None
        if new_price < 10:
            print("ERROR: Price must be 1More than $10 CAD")
            return None
        product_to_be_updated.product_price = new_price
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
        product_exists = Product.query.filter_by(product_title=new_title).all()
        if len(product_exists) > 0:
            print("ERROR: Product Must Be Unique")
            return None
        product_to_be_updated.product_title = new_title
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


class Review(db.Model):
    """
    Class to represent a product review
    
    Attributes:
        - id - to identify the review in the system and to be easily queried
        - user_email - identifies the owner that created the review
        - score - a score out of 10, 10 being great, 0 being awful
        - review - body of text that supports the overall score 
    """
    __tablename__ = 'Review'
    review_ID = db.Column(db.Integer, primary_key=True)
    reviewer_email = db.Column(db.String(80), db.ForeignKey('User.user_email'),
                               nullable=False)
    score = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(150), nullable=True)

    def __repr__(self):
        return """<Review(review_ID= {}, reviewer_email= {}, score= {}, 
                  review= {}>""".format(self.review_ID,
                                        self.reviewer_email, 
                                        self.score, 
                                        self.review)
    

def create_review(email, score, review):
    global number_of_reviews
    review_creator = User.query.filter_by(user_email=email)
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
    review = Review(review_ID=number_of_reviews, reviewer_email=email, 
                    score=score, review=review)  
    # create the product object
    db.session.add(review)
    db.session.commit()  # add product to db and save
    number_of_reviews += 1  # this value used to create unique ID
    return True
    

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
    transaction_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_email = db.Column(db.String(80), db.ForeignKey('User.user_email'),
                           nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('Product.product_ID'),
                           nullable=False)
    price = db.Column(db.Integer, db.ForeignKey('Product.product_price'),
                      nullable=False) 
    date = db.Column(db.String(80), primary_key=True)

    def __repr__(self):
        return """<Transaction(transaction_ID= {}, user_email= {}, 
                  product_id= {}, review= {}>""".format(self.transaction_id,
                                                        self.user_email, 
                                                        self.product_id, 
                                                        self.price, self.date)


def create_transaction(email, product_id, price):
    global number_of_transactions
    buyer_email = User.query.filter_by(user_email=email)
    if buyer_email is None:
        print("ERROR: Account Not registered please create an account")
        return False
    product_id_search = Product.query.filter_by(product_ID=product_id)
    if product_id_search is None:
        print("ERROR: Account Not registered please create an account")
        return False
    price_search = Product.query.filter_by(product_price=price)
    if price_search is None:
        print("ERROR: Account Not registered please create an account")
        return False
    todays_date = date.today() 
    id = number_of_transactions
    transaction = Transaction(transaction_id=id, user_email=email, 
                              product_id=product_id, price=price, 
                              date=todays_date)  
    # create the product object
    db.session.add(transaction)
    db.session.commit()  # add product to db and save
    number_of_transactions += 1  # this value used to create unique ID
    return True


db.create_all()  # creating database and columns from qbay