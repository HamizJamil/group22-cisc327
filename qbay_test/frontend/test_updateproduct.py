from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import Product
from selenium import webdriver


class FrontEndUpdateProductTest(BaseCase):

    def test_update_product(self, *_):
        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")  # insert the text fields
        self.type("#title", "Gloves")
        self.type("#new_title", "Winning")
        self.type("#new_price", 350)
        self.type("#new_description", "High end Japanese boxing gloves")
        self.find_element("#Submit").click()

        new_prod = Product.query.filter_by(
            title="Winning", owner_email="test0@test.com").first()

        assert new_prod is not None \
               and new_prod.description == "High end Japanese boxing gloves"
