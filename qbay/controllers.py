from flask import redirect, url_for, render_template
from flask import request, session, flash
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
            session.permanent = True
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
        title = request.form["title"]
        if title.startswith(" ") or title.endswith(" ") or \
                not title.replace(" ", "").isalnum():
            flash("The title of the product has to be alphanumeric-only, "
                  "and space allowed only if it is not as prefix and suffix")
            return render_template("createproduct.html")
        if len(title) > 80:
            flash("The title's too long")
            return render_template("createproduct.html")

        description = request.form["description"]
        if len(description) < len(title) or len(description) < 20 \
                or len(description) > 2000:
            flash("Description needs to be longer than the title and between"
                  " 20 and 2000 characters long")
            return render_template("createproduct.html")
        found_prod = Product.query.filter_by(title=title).first()
        if found_prod:
            flash("This product is already created! Please use update or "
                  "add a new title")
            return render_template("createproduct.html")
        else:
            price = request.form["price"]
            product = Product(title, price, description, owner_email)
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
        password2 = request.form["user_pass2"]
        user_name = request.form["user_name"]
        if password != password2:
            flash("Passwords mismatch. Please Enter again!")
            return redirect(url_for("registration"))
        found_user = User.query.filter_by(email=email).first()
        if found_user:
            flash("This user is already registered! Please log in:")
            return redirect(url_for("login"))
        # if email provided is not RFC 5322
        if email_regex.search(email) is None:
            flash("Please provide a valid email address")
            return redirect(url_for("registration"))

        if user_name.startswith(" ") or user_name.endswith(" "):
            flash("User name can't start or end with a space.")
            return redirect(url_for("registration"))
        if not user_name.isalnum():
            flash("User name has to be alpha-numeric.")
            return redirect(url_for("registration"))
        if len(user_name) < 2 or len(user_name) > 20:
            flash("User name has to be between 2 and 20 characters long.")
            return redirect(url_for("registration"))

        if password_regex.search(password) is None:
            flash("Password has to be minimum length 6,"
                  " at least one upper case, at least one lower case,"
                  " and at least one special character [!@#$%^&+=]", "info")
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
        session.permanent = True
        usr = session["user"]
        session.pop(usr, None)
        session["user"] = ""
        flash("You have been logged out successfully!", "info")
        return render_template("home.html")
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
    if request.method == "POST":
        if postal_code_regex.search(request.form["postal_code"]) is None:
            flash("postal code should be X9X9X9")
            return render_template("updateprofile.html")
        user_found = User.query.filter_by(email=session["user"]).first()
        user_found.postal_code = request.form["postal_code"]
        user_found.shipping_address = request.form["shipping_address"]
        db.session.commit()
        return render_template("userhome.html")
    else:
        return render_template("updateprofile.html")


@app.route("/updateproduct", methods=["POST", "GET"])
def update_product():
    if request.method == "POST":
        title = request.form["title"]
        prod_found = Product.query.filter_by(title=title).first()
        if prod_found is None:
            flash("record Not found")
            return render_template("updateproduct.html")
        else:
            if request.form["Description"]:
                len_desc = len(request.form["Description"])
                if len_desc < len(title) or len_desc < 20 \
                        or len_desc > 2000:
                    flash("Description needs to be longer than the title "
                          "and between 20 and 2000 characters long")
                else:
                    prod_found.description = request.form["Description"]
            if request.form["price"]:
                prod_found.price = request.form["price"]
            prod_found.last_modified_date = date.today()
            db.session.commit()
            return render_template("updateproduct.html")
    else:
        return render_template("updateproduct.html")


@app.route("/userhome", methods=["POST", "GET"])
def user_home():
    return render_template("userhome.html")
