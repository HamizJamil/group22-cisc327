from flask import Flask, redirect, url_for, render_template
from flask import request, session, flash
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import flag_modified
from qbay import app
from qbay.models import *


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["user_email"]
        password = request.form["user_pass"]
        session.permanent = True
        found_user = User.query.filter_by(email=email).first()
        if found_user and password == found_user.password:
            session["user"] = email
            return render_template("userhome.html")
        else:
            flash("The email or password provided are wrong")
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/createproduct", methods=["POST", "GET"])
def create_product():
    if request.method == "POST":
        owner_email = request.form["user_email"]
        print(owner_email)
        curr_user = User.query.filter_by(email=owner_email).first()
        title = request.form["title"]
        description = request.form["description"]
        found_Prod = Product.query.filter_by(title=title).first()
        print(title, len(title))
        if title.startswith(" ") or title.endswith(" ") or \
                not title.replace(" ", "").isalnum():
            flash("The title of the product has to be alphanumeric-only, "
                  "and space allowed only if it is not as prefix and suffix")
            return render_template("createproduct.html")
        elif len(title) > 80:
            flash("The title's too long")
            return render_template("createproduct.html")
        elif len(description) < len(title) or len(description) < 20 \
                or len(description) > 2000:
            flash("Description needs to be longer than the title and between"
                  "20 adn 2000 characters long")
            return render_template("createproduct.html")
        elif found_Prod:
            flash("This product is already created! Please use update or" +
                  "add a new title")
            return render_template("createproduct.html")
        elif not curr_user:
            flash("Sorry must have a valid Qbay account to create a product")
            return render_template("createproduct.html")
        else:
            price = request.form["price"]
            product = Product(title, int(price), description, owner_email)
            db.session.add(product)
            db.session.commit()
            return render_template("userhome.html")
    else:
        return render_template("createproduct.html")


@app.route("/registration", methods=["POST", "GET"])
def registration():
    if request.method == "POST":
        email = request.form["user_email"]
        session["user"] = email
        session.permanent = True
        password = request.form["user_pass"]
        user_name = request.form["user_name"]
        found_user = User.query.filter_by(email=email).first()
        if found_user is not None:
            flash("This user is already registered! Please log in:")
            return redirect(url_for("login"))
        elif email_regex.search(email) is None: 
            # if email provided is not RFC 5322
            flash("Please provide a valid email address")
            return redirect(url_for("registration"))
        elif user_name.startswith(" ") or user_name.endswith(" "):
            flash("User name can't start or end with a space.")
            return redirect(url_for("registration"))
        elif not user_name.isalnum():
            flash("User name has to be alpha-numeric.")
            return redirect(url_for("registration"))
        elif len(user_name) < 2 or len(user_name) > 20:
            flash("User name has to be between 2 and 20 characters long.")
            return redirect(url_for("registration"))
        elif password_regex.search(password) is None:
            flash("Password has to be minimum length 6,"
                  " at least one upper case, at least one lower case,"
                  " and at least one special character [@#$%^&+=]", "info")
            return redirect(url_for("registration"))
        else:
            usr = User(email, user_name, password)
            db.session.add(usr)
            db.session.commit()
            return redirect(url_for("login"))
    else:
        return render_template("registration.html")


@app.route("/logout", methods=["POST", "GET"])
def logout():
    if request.method == "POST":
        session.permanent(True)
        usr = session["user"]
        session.pop("usr", None)
        flash("You have been logged out successfully!", "info")
        return redirect(url_for("logout.html", usr))
    else:
        return render_template("home.html")


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["user_email"]
        session["user"] = user
        return render_template("home.html")
    else:
        return render_template("home.html")


@app.route("/updateprofile", methods=["POST", "GET"])
def update_profile():
    print("user profile")
    user_found = User.query.filter_by(email=session["user"]).first()
    print(user_found)
    if request.method == "POST":
        print(request.form["shipping_address"])
        print(request.form["postal_code"])
        user_found.postal_code = request.form["postal_code"]
        if postal_regex.search(user_found.postal_code) is None:
            flash("ERROR: Please enter a valid postal code", "info")
        user_found.shipping_address = request.form["shipping_address"]
        db.session.commit()
    return render_template("updateprofile.html")


@app.route("/updateproduct", methods=["POST", "GET"])
def update_product():
    if request.method == "POST":
        title = request.form["title"]
        Prod_found = Product.query.filter_by(title=title).first()
        print(Prod_found)
        if Prod_found is None:
            flash("record Not found")
        else:
            Prod_found.description = request.form["Description"]
            Prod_found.price = request.form["price"]
            db.session.commit()
            return render_template("updateproduct.html")
    else:
        return render_template("updateproduct.html")


@app.route("/userhome", methods=["POST", "GET"])
def user_home():
    return render_template("userhome.html")
