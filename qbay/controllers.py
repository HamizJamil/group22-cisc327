from flask import Flask, redirect, url_for, render_template
from flask import request, session, flash

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import flag_modified
from qbay import app
from qbay.models import *


# authenticates user currently in an active session with qBay
def authenticate(req_email):
    authorized = True
    if "user_email" not in session or req_email != session["user_email"]:
        flash("User is not authorized, please login")
        authorized = False
    return authorized


# gets the login page for the user
@app.route('/login', methods=['GET'])
def login_get():
    if "user_email" in session:
        render_template("userhome.html")
    return render_template("login.html")


# sends login information to backend and returns home page if successful
@app.route('/login', methods=["POST"])
def login_post():
    email = request.form["user_email"]
    password = request.form["user_pass"]
    found_user = login(email, password, error_handler)
    if found_user:
        session.permanent = True
        session["user_email"] = email
        return render_template("userhome.html")
    else:
        flash("user and/or password mismatched")
        return render_template("login.html")


# gets the create product page for the user
@app.route("/createproduct", methods=["GET"])
def create_product_get():
    return render_template("createproduct.html")


# sends new product information to backend to be added to DB
@app.route("/createproduct", methods=["POST"])
def create_product_post():
    user_email = request.form.get("user_email")
    if not authenticate(user_email):
        return redirect("/login")
    current_user = User.query.filter_by(email=user_email).first()
    title = request.form.get("title")
    description = request.form.get("description")
    price = float(request.form.get("price"))
    new_product = create_product(title, description, user_email,
                                 price, error_handler)
    if new_product:
        flash("Product Created Successfully!")
        return render_template("userhome.html")
    else:
        return render_template("createproduct.html")


# if POST request, sends registration information to backend DB
# if GET request, returns HTML page for registration to the user
@app.route("/registration", methods=["POST", "GET"])
def registration():
    if request.method == "POST":
        email = request.form.get("user_email")
        password = request.form.get("user_pass")
        user_name = request.form.get("user_name")
        found_user = register_user(user_name, email, password, error_handler)
        if found_user:
            return render_template("userhome.html")
        else:
            return render_template("registration.html")
    else:
        return render_template("registration.html")


# removes user from logged in session and returns them to login page
@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user_email", None)
    flash("You have been logged out successfully!", "info")
    return redirect("/login")


# redirects users to login if they are not currently in an active
# session, if they are it redirects them to the home page
@app.route("/", methods=["GET"])
def home():
    if "user_email" in session:
        return render_template("home.html")
    else:
        return redirect("/login")


# if POST request, sends updated profile info to backend DB
# if GET request, returns update profile page for user
@app.route("/updateprofile", methods=["POST", "GET"])
def update_profile():
    if request.method == "POST":
        email = request.form["user_email"]
        if not authenticate(email):
            return redirect("/login")
        new_username = request.form["user_name"]
        shipping_address = request.form["shipping_address"]
        postal_code = request.form["postal_code"]
        updated = update_user(email, new_username, shipping_address,
                              postal_code, error_handler)
        if updated:
            flash("Information Successfully Updated!")
        return render_template("updateprofile.html")
    else:
        return render_template("updateprofile.html")


# returns update product page to the user
@app.route("/updateproduct", methods=["GET"])
def update_product_get():
    return render_template("updateproduct.html")


# sends updated product information submitted by user to backend DB
@app.route("/updateproduct", methods=["POST"])
def update_product_post():
    title = request.form.get("title")
    email = request.form.get("email")
    if not authenticate(email):
        return redirect("/login")
    new_price = request.form.get("new_price")
    new_title = request.form.get("new_title")
    new_description = request.form.get("new_description")
    updated = update_product(title, email, new_price, new_title,
                             new_description, error_handler)
    if updated:
        flash("Product Successfully Updated!")
        return render_template("userhome.html")
    else:
        return render_template("updateproduct.html")


# redirects user to their homepage
@app.route("/userhome", methods=["GET"])
def user_home():
    return render_template("userhome.html")


# redirects user to the product page for them to browse
@app.route("/products", methods=["GET"])
def products():
    email = session["user_email"]
    list_of_products = display_products(email)
    return render_template("products.html", query=list_of_products)


# upon product purchase, sends product id and user to backend DB
# and calls on create_transaction function to complete purchase
@app.route("/buy_product/<int:product_id>/", methods=["GET"]) 
def buy_product(product_id):
    current_user = session["user_email"]
    success = create_transaction(current_user, product_id, error_handler)
    if success:
        flash("Product successfully purchased")
        return render_template("userhome.html")
    else:
        return redirect("/products")