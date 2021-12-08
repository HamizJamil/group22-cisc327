from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from qbay.models import Product, Transaction, create_product, login
from qbay.models import register_user


class BuyProductFrontendTest(BaseCase):
    # test if buy product works
    def test_buy_product1(self, *_):
        # register user to db, login as user,
        # and create product, then retrieve product id and title.
        register_user("Test1738", "test12345@gmail.com", "Test1234!")
        login("test12345@gmail.com", "Test1234!")
        create_product("Cool test product", "This product is goated, "
                       + "please buy it!", "test12345@gmail.com", 50)
        prod = Product.query.filter_by(title="Cool test product").first()
        prod_id = prod.id
        # login as user buying
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()
        # buy product
        self.open(base_url + "/products")
        self.open(base_url + "/buy_product/" + str(prod_id) + "/")
        # check that no product is created
        new_transact = Transaction.query.filter_by(id=prod_id).all()
        assert new_transact is not None

    # test trying to buy own product
    def test_buy_product2(self, *_):
        # register user to db, login as user,
        # and create product, then retrieve product title and id.
        register_user("Test1932", "test1234@gmail.com", "Test12345!") 
        login("test1234@gmail.com", "Test12345!")
        create_product("Cool test product 2", "This product is goated, please"
                       + " buy it :)", "test1234@gmail.com", 60)
        prod = Product.query.filter_by(title="Cool test product 2").first()
        prod_id = prod.id
        # buy product
        self.open(base_url + "/products")
        self.open(base_url + "/buy_product/" + str(prod_id) + "/")
        # check that no product is created
        new_transact = Transaction.query.filter_by(id=prod_id).first()
        assert new_transact is None

    def test_buy_product3(self, *_):
        # login as seller, and create product,
        # then retrieve product title and id.
        login("test1234@gmail.com", "Test12345!")
        create_product("Cool test product 3", "This product is goated, please"
                       + " buy it <3", "test1234@gmail.com", 600)
        prod = Product.query.filter_by(title="Cool test product 2").first()
        prod_id = prod.id
        # login as buyer
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()
        # buy product
        self.open(base_url + "/products")
        self.open(base_url + "/buy_product/" + str(prod_id) + "/")
        # check that no product is created
        new_transact = Transaction.query.filter_by(id=prod_id).first()
        assert new_transact is None
