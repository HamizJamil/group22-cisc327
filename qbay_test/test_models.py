from qbay.models import *


# using assert keyword to run checks 
def test_r1_user_register():
    assert register_user('u0X', 'test0@test.com', 'eA123456!') is True
    assert register_user('u0X', 'test1@test.com', 'eA123456!') is True
    assert register_user('u0X', 'test0@test.com', '123456') is False


def test_r2_login():
    user = login('test0@test.com', 'eA123456!')
    assert user is not None
    assert (user.user_name == 'u0X') is True
    
    user = login('test0@test.com', 'eA123456')
    assert user is None


def test_r3_user_update():  
    assert update_user('test0@test.com', 'u1X', '99 University Ave Kingston', 
                       'K7L 3N6') is not None
    assert update_user('test1@test.com', 'u1X', '9! University Ave Kingston ',
                       'K7L 3N6') is None


def test_r4_product_create():
    assert create_product('iPhone11X New', 'Brand New iPhone11X 2020',
                          'test0@test.com', 600) is True
    assert create_product('iPhone11X Pro', 'This iPhone is so powerful',
                          'test1@test.com', 1000) is True
    assert create_product('iPhone11X', ' New ', 'test0@test.com', 10) is False


def test_r5_product_update():
    assert update_product('iPhone11X New', 'test0@test.com', 1000, 
                          "Coolest Phone Ever", None) is not None
    assert update_product('iPhone11X Pro', 'test1@test.com', 1500, None, 
                          "256GB storage and fast") is not None
    assert update_product('iPhone11X New', 10001, "Coolest Phone Ever", None
                          ) is None


def test_r6_create_review():
    assert create_review('test1@test.com', 6, "This phone is so good") is True
    assert create_review('test0@test.com', "Six", "This phone is so good"
                         ) is False


def test_r7_create_transaction():
    product_bought = Product.query.filter_by(product_title='iPhone11X Pro'
                                             ).first()
    ID = product_bought.product_ID
    price = product_bought.product_price
    assert create_transaction('test1@test.com', ID, price)