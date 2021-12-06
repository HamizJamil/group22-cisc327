from flask import Flask, redirect, url_for, render_template
from flask import request, session, flash

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import flag_modified
from qbay import app
from qbay.models import *


def authenticate(req_email):
    authorized = True
    if "user_email" not in session or req_email != session["user_email"]:
        flash("Uer is not authorized, please login")
        authorized = False
    return authorized


@app.route('/login', methods=['GET'])
def login_get():
    if "user_email" in session:
        render_template("userhome.html")
    return render_template("login.html")


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


@app.route("/createproduct", methods=["GET"])
def create_product_get():
    return render_template("createproduct.html")


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


@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user_email", None)
    flash("You have been logged out successfully!", "info")
    return redirect("/login")


@app.route("/", methods=["GET"])
def home():
    if "user_email" in session:
        return render_template("home.html")
    else:
        return redirect("/login")


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


@app.route("/updateproduct", methods=["GET"])
def update_product_get():
    return render_template("updateproduct.html")


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


@app.route("/userhome", methods=["GET"])
def user_home():
    return render_template("userhome.html")

@app.route("/products", methods=["GET"])
def products():
    email = session["user_email"]
    list_of_products = display_products(email)
    return render_template("products.html", query=list_of_products)
