import os
from qbay.models import Product, User


def pytest_sessionstart():
    print("Initializing Environment...")
    db_file = 'db.sqlite'
    if os.path.exists(db_file):  # checking if file already exists
        os.remove(db_file)  # remove if so
    User.query.delete()
    Product.query.delete()
