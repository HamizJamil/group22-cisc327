from flask import Flask, redirect, url_for, render_template
from datetime import date
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app)


# declaring the User model
class User(db.Model):
    user_name = db.Column(db.String(20), primary_key=True)
    email = db.Column(db.String(50), index=True, unique=True)
    shipping_address = db.Column(db.String(100), index=True, unique=False)
    postal_code = db.Column(db.String(7), index=True, unique=False)
    balance = db.Column(db.Integer, index=True, unique=False)
    # relationship between User and other Models
    products=db.relationship('Product', backref='user', lazy='dynamic')
    reviews = db.relationship('Review', backref='user', lazy='dynamic')
    transactions = db.relationship('Transaction', backref='user', lazy='dynamic')

    def __repr__(self):
        return "User: {}".format(self.user_name)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True, unique=False)
    description=db.Column(db.String(200), index=True, unique=False)
    price=db.Column(db.Float, index=True, unique=False)
    # last_modified_date=db.Column(db.Date, index=True, unique=False)
    owner_email = db.Column(db.String, db.ForeignKey('user.user_name'))
    transactions = db.relationship('Transaction', backref='product', lazy='dynamic')
    reviews = db.relationship('Review', backref='product', lazy='dynamic')

    def __repr__(self):
        return "Product {}: {} Price: {}".format(self.id, self.title, self.price)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Float, index=True, unique=False)
    # date = db.Column(db.Date, index=True, unique=False)
    buyer = db.Column(db.String, db.ForeignKey('buyer.user_name'))
    seller = db.Column(db.String, db.ForeignKey('seller.user_name'))
    product = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __repr__(self):
        return "Transaction {}: {}, date: {}".format(self.id, self.product,
                                                     self.date)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, unique=False)
    text = db.Column(db.String(200), unique=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    reviewer_user_name = db.Column(db.String, db.ForeignKey('user.user_name'))

    #get a nice printout for Review objects
    def __repr__(self):
        return "Review: {} stars: {}".format(self.text, self.stars)

#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
