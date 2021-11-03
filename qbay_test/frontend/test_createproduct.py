from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import Product
from selenium import webdriver


class FrontEndProductCreationTest(BaseCase):
    
    # SMOKE TESTS FOR CREATE PRODUCT
    # checking if submit and fill works
    def test_create_product_1(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "Iphone 11 Max Pro")
        self.type("#price", 1000)
        self.type("#description", "Brand-New, so good and fast")
        self.find_element("#Save").click()
        # veryfing that it redirects to homepage
        self.assert_title("Home Page")  
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="Iphone 11 Max Pro").all()
        assert new_prod is not None 

    # veryfing back button functionality and routing
    # no product should be submitted to db
    def test_create_product_2(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "Super cool new phone")
        self.type("#price", 1000)
        self.type("#description", "You wish your phone was this good")
        self.find_element("#Back").click()
        # veryfing that it redirects to homepage
        self.assert_title("Home Page")  
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="Super cool new phone"
                                           ).first()
        assert new_prod is None 

    # BOUNDARY TESTS FOR CREATE PRODUCT
    #  Checking when character title length is 1 char
    def test_create_product_3(self, *_):  
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "1")
        self.type("#price", 1000)
        self.type("#description", "You wish your phone was this good")
        self.find_element("#Save").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="1").first()
        assert new_prod is not None

    # checking when title length is 80 char
    def test_create_product_4(self, *_): 
        bad_title = ("111111111111111111111111111111111111111111111111111111" +
                    "11111111111111111111111111")
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", bad_title)
        self.type("#price", 1000)
        self.type("#description", "11111111111111111111111111111111111111111" +
                  "1111111111111111111111111111111111111111")
        self.find_element("#Save").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title=bad_title).first()
        assert new_prod is not None

    # veryfying error when description is 20 char long
    def test_create_product_5(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "Test5")
        self.type("#price", 1000)
        self.type("#description", "12345678910111213141")
        self.find_element("#Save").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="Test5").first()
        assert new_prod is not None
    
    # veryfying error when description is 2000 char long
    def test_create_product_6(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "Test5")
        self.type("#price", 1000)
        self.type("#description", "11111111111111111111111111111111111111111" + 
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111")
        self.find_element("#Save").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="Test5").first()
        assert new_prod is not None

    # verfifying creation of product when price $10
    def test_create_product_7(self, *_):  
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "3")
        self.type("#price", 10)
        self.type("#description", "You wish your phone was this good")
        self.find_element("#Save").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="3").first()
        assert new_prod is not None
    
    # verfifying creation of product when price $10000
    def test_create_product_8(self, *_):  
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "4")
        self.type("#price", 10000)
        self.type("#description", "You wish your phone was this good")
        self.find_element("#Save").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="4").first()
        assert new_prod is not None
    
    #  Checking when character title length is 0 char
    def test_create_product_9(self, *_):  
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "")
        self.type("#price", 1000)
        self.type("#description", "You wish your phone was this good")
        self.find_element("#Save").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None
        self.assert_element('#alert')

    #  Checking when character title length is 81 char
    def test_create_product_10(self, *_):
        bad_title = ("111111111111111111111111111111111111111111111111111111" +
                    "111111111111111111111111111")  
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", bad_title)
        self.type("#price", 1000)
        self.type("#description", "You wish your phone was this good")
        self.find_element("#Save").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title=bad_title).first()
        assert new_prod is None
        self.assert_element('#alert')

    
    #  Checking when character description length is 2001 char
    def test_create_product_11(self, *_):  
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "2")
        self.type("#price", 1000)
        self.type("#description", "11111111111111111111111111111111111111111" + 
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "111111111111111111111111111111111111111111111111111111111" +
                  "1111111111111111111111")
        self.find_element("#Save").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="2").first()
        assert new_prod is None
        self.assert_element('#alert')