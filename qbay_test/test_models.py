from qbay.models import create_product, update_product
from qbay.models import register_user, login
from qbay_test.conftest import pytest_sessionstart
from qbay.models import User, Product

pytest_sessionstart() # clearing out db before testing to repeat w same row

# using assert keyword to run checks 
def test_r1_user_register():
    assert register_user('u0X', 'test0@test.com', 'eA123456!') is True
    assert register_user('u0X', 'test1@test.com', 'eA123456!') is True
    assert register_user('u0X', 'test0@test.com', '123456') is False
    print(User.query.all())

def test_r2_login():
    user = login('test0@test.com', 'eA123456!') is True
    assert user is not None
    assert user.user_name == 'u0X' is True

    user = login('test0@test.com', 'eA123456')
    assert user is None

# title, description, owner_email, price
def test_r3_product_create():
    assert create_product('iPhone11X New', 'Brand New iPhone11X 2020',\
                          'test0@test.com' ,600) is True
    assert create_product('iPhone11X Pro', 'This iPhone is so powerful',\
                         'test1@test.com!', 1000) is True
    assert create_product('iPhone11X', ' New ', 'test0@test.com', 10) is False


def test_r4_product_update():
    pass
