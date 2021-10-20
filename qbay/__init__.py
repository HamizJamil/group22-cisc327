from flask import Flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))  
# accessing proper directory for db file
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
