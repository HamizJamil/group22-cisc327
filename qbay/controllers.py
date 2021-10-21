from flask import render_template, request, session, redirect
from qbay.models import *

from qbay import app


@app.route('/')
def home(user):
    # authentication still required

    # fake product data below
    products = [
        {'name': 'Watch', 'price': 10, 'product_id': 1},
        {'name': 'Shoes', 'price': 15, 'product_id': 2}
    ]
    return render_template('index.html', user=user, products=products)


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = login(email, password)
    if user is None: 
        return render_template('login.html', 
                               message='Invalid login credentials')
    else:
        session['user_email'] = user.email 
        # user is successfully logged in, return to home page
        return redirect('/', code=303)


@app.route('/logout')
def logout():
    if 'user_email' in session:
        session.pop('user_email', None)
    return redirect('/login')

