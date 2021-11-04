from flask import Flask, redirect, url_for, render_template
from flask import request, session, flash
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import flag_modified
from qbay import app
from qbay.models import *


@app.route('/login', methods=['GET'])
def login_get():
    return render_template("login.html")


@app.route('/login', methods=["POST"])
def login_post():
    email = request.form["user_email"]
    password = request.form["user_pass"]
    session.permanent = True
    found_user = login(email, password, error_handler)
    if found_user:
        session["user"] = email
        return render_template("userhome.html")
    else:
        return render_template("login.html")


@app.route("/createproduct", methods=["GET"])
def create_product_get():
    return render_template("createproduct.html")


@app.route("/createproduct", methods=["POST"])
def create_product_post():
    user_email = request.form.get("user_email")
    current_user = User.query.filter_by(email=user_email).first()
    title = request.form.get("title")
    description = request.form.get("description")
    price = int(request.form.get("price"))
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
        session["user"] = email
        session.permanent = True
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
    usr = session["user"]
    session.pop("usr", None)
    flash("You have been logged out successfully!", "info")
    return redirect("/login")


@app.route("/", methods=["GET"])
def home():
    user = request.form.get("user_email")
    session["user"] = user
    return render_template("home.html")


@app.route("/updateprofile", methods=["POST", "GET"])
def update_profile():
    if request.method == "POST":
        email = request.form["user_email"]
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
