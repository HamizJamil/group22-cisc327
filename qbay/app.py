from flask import Flask, redirect, url_for, render_template, request , session , flash
# from datetime import date
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "mykey"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
# db = SQLAlchemy(app)


# # declaring the User model
# class User(db.Model):
#     user_name = db.Column(db.String(20), primary_key=True)
#     email = db.Column(db.String(50), index=True, unique=True)
#     shipping_address = db.Column(db.String(100), index=True, unique=False)
#     postal_code = db.Column(db.String(7), index=True, unique=False)
#     balance = db.Column(db.Integer, index=True, unique=False)
#     # relationship between User and other Models
#     products=db.relationship('Product', backref='user', lazy='dynamic')
#     reviews = db.relationship('Review', backref='user', lazy='dynamic')
#     transactions = db.relationship('Transaction', backref='user', lazy='dynamic')
#
#     def __repr__(self):
#         return "User: {}".format(self.user_name)
#
#
# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50), index=True, unique=False)
#     description=db.Column(db.String(200), index=True, unique=False)
#     price=db.Column(db.Float, index=True, unique=False)
#     # last_modified_date=db.Column(db.Date, index=True, unique=False)
#     owner_email = db.Column(db.String, db.ForeignKey('user.user_name'))
#     transactions = db.relationship('Transaction', backref='product', lazy='dynamic')
#     reviews = db.relationship('Review', backref='product', lazy='dynamic')
#
#     def __repr__(self):
#         return "Product {}: {} Price: {}".format(self.id, self.title, self.price)
#
#
# class Transaction(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     price = db.Column(db.Float, index=True, unique=False)
#     # date = db.Column(db.Date, index=True, unique=False)
#     buyer = db.Column(db.String, db.ForeignKey('buyer.user_name'))
#     seller = db.Column(db.String, db.ForeignKey('seller.user_name'))
#     product = db.Column(db.Integer, db.ForeignKey('product.id'))
#
#     def __repr__(self):
#         return "Transaction {}: {}, date: {}".format(self.id, self.product,
#                                                      self.date)
#
#
# class Review(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     stars = db.Column(db.Integer, unique=False)
#     text = db.Column(db.String(200), unique=False)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
#     reviewer_user_name = db.Column(db.String, db.ForeignKey('user.user_name'))
#
#     #get a nice printout for Review objects
#     def __repr__(self):
#         return "Review: {} stars: {}".format(self.text, self.stars)
@app.route("/login" ,methods=["POST","GET"])
def login():
    if request.method == "POST":
        usr=request.form.get("user_email")
        paswrd=request.form.get("pass2")
        if (usr== None):
            return render_template("Login.html")
        else:
            return render_template("UserHome.html")
    else:
        return render_template("Login.html")

@app.route("/Registration")
def Registration():
    return render_template("Registration.html")

@app.route("/Logout",methods=["POST","GET"])
def logout():
    if request.method == "POST":
        usr=session["user"]
        session.pop("usr", None)
        flash("You have been logged out successfully!", "info")
        return redirect(url_for("Logout.html",usr))
    else:
        return render_template("home.html")

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        user=request.form["user_email"]
        session["user"] = user
        return render_template("home.html")
    else:
        return render_template("home.html")


@app.route("/CreateProduct", methods=["POST","GET"])
def CreateProduct():
    if request.method == "POST":
       return redirect(url_for("/"))
    else:
        return render_template("CreateProduct.html")

@app.route("/UpdateProfile")
def Update_Profile():
    return render_template("UpdateProfile.html")

@app.route("/UpdateProduct" , methods=["POST","GET"])
def UpdateProduct():
    if request.method == "POST":
        return redirect(url_for("/"))
    else:
        return render_template("UpdateProduct.html")

@app.route("/UserHome" , methods=["POST","GET"])
def UserHome():
    return render_template("UserHome.html")

# @app.route("/admin")
# return redirect(url_for("user", name="Admin!"))  # Now we when we go to /admin we will redirect to user with the argument "Admin!"

if __name__ == "__main__":
    app.run(debug=True)

