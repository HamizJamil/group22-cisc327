from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import Product


class FrontEndProductCreationTest(BaseCase):
    
    # Smoke Test For Create Product
    def test_create_product_1(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "Iphone 11 Max Pro")
        self.type("#price", 1000)
        self.type("#description", "Brand-New, so good and fast")
        self.click('input[type="submit"]')
    


