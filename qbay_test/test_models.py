from qbay.models import *


# using assert keyword to run checks with global backend functions
def test_register_update():
    assert register_user('profiletest', 'update@gmail.com', 'ABC@abc') is True


def test_r1_user_register():
    # checking 3 different user situations where 3rd pw is missing special char
    assert register_user('u0X', 'test0@test.com', 'eA123456!') is True
    assert register_user('u0X', 'test1@test.com', 'eA123456!') is True
    assert register_user('u0X', 'test0@test.com', '123456') is False


def test_r2_login():
    # checking a fake user login and verifying its username credential
    user = login('test0@test.com', 'eA123456!')
    assert user is not None
    assert (user.user_name == 'u0X') is True
    # testing login with wrong credentials
    user = login('test0@test.com', 'eA123456')
    assert user is None


def test_r3_user_update():
    # taking passed users from r1 and and checking that the added addy/postal
    # code is valid by returning a user object
    assert update_user('test0@test.com', 'u1X', '99 University Ave Kingston',
                       'K7L 3N6') is not None
    # testing with incorrect addy sequence resulting in no returned user
    assert update_user('test1@test.com', 'u1X', '9! University Ave Kingston ',
                       'K7L 3N6') is None


def test_r4_product_create():
    # testing creating a product with proper credentials
    assert create_product('iPhone11X New', 'Brand New iPhone11X 2020',
                          'test0@test.com', 600) is True
    # testing creating a product with different correct credentials
    assert create_product('iPhone11X Pro', 'This iPhone is so powerful',
                          'test1@test.com', 1000) is True
    # testing product failure with too small of description
    assert create_product('iPhone11X', ' New ', 'test0@test.com', 10) is False


def test_r5_product_update():
    # testing updating a prodcut with new description and price
    assert update_product('iPhone11X New', 'test0@test.com', 1000,
                          "Coolest Phone Ever", None) is not None
    assert update_product('iPhone11X Pro', 'test1@test.com', 1500, None,
                          "256GB storage and fast") is not None
    # incorrectily updating product with price decrease
    assert update_product('iPhone11X New', 10001, "Coolest Phone Ever", None
                          ) is None


def test_r6_create_review():
    # creating a review with int score
    assert create_review('test1@test.com', 6, "This phone is so good") is True
    # creating bad review with text score
    assert create_review('test0@test.com', "Six", "This phone is so good"
                         ) is False


def test_r7_create_transaction():
    # check transaction with valid product
    product_bought = Product.query.filter_by(title='iPhone11X Pro'
                                             ).first()
    price = product_bought.price
    assert create_transaction('test1@test.com', price) is True
