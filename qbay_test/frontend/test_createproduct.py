from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import Product
from selenium import webdriver


class FrontEndProductCreationTest(BaseCase):
    
    # Smoke Test For Create Product - checking if submit and fill works
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
        new_prod = Product.query.filter_by(title="Super cool new phone").first()
        assert new_prod is None 
    

    
    
        
    


