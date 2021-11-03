from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import Product
from selenium import webdriver

two_thousand_char_description = ("11111111111111111111111111111111111111111" +
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
bad_title = ("111111111111111111111111111111111111111111111111111111" +
                    "11111111111111111111111111")
                  
class FrontEndProductCreationTest(BaseCase):
    
    # SMOKE TESTS FOR CREATE PRODUCT
    # checking if submit and fill works
    def test_create_product_1(self, *_):
        self.open(base_url + '/createproduct')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#title", "Iphone 11 Max Pro")
        self.type("#price", 1000)
        self.type("#description", "Brand-New, so good and fast")
        self.find_element("#Save").click()  # click save to submit
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
        global bad_title
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
        self.type("#title", "Test6")
        self.type("#price", 1000)
        self.type("#description", two_thousand_char_description)
        self.find_element("#Save").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="Test6").first()
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

    # veryfying error when description is 19 char long
    def test_create_product_11(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "Test11")
        self.type("#price", 1000)
        self.type("#description", "1234567891011121314")
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="Test11").first()
        assert new_prod is None
        self.assert_element('#alert')

    #  Checking when character description length is 2001 char
    def test_create_product_12(self, *_): 
        global two_thousand_char_description 
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "2")
        self.type("#price", 1000)
        self.type("#description", two_thousand_char_description + "1")
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="2").first()
        assert new_prod is None

    # veryfying error when price is 9
    def test_create_product_13(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "Test13")
        self.type("#price", 9)
        self.type("#description", "Description Valid")
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="Test13").first()
        assert new_prod is None

    # veryfying error when price is 10001
    def test_create_product_14(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "Test14")
        self.type("#price", 10001)
        self.type("#description", "Description Valid")
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="Test14").first()
        assert new_prod is None

    # veryfying Condition FFFF error
    def test_create_product_15(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0wq@test.com")
        self.type("#title", "")
        self.type("#price", 9)
        self.type("#description", two_thousand_char_description + "1")
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None
    
    # veryfying Condition FFFT error
    def test_create_product_16(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0wq@test.com")
        self.type("#title", "")
        self.type("#price", 9)
        self.type("#description", two_thousand_char_description)
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None
    
    # veryfying Condition FFTF error
    def test_create_product_17(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0wq@test.com")
        self.type("#title", "")
        self.type("#price", 10)
        self.type("#description", two_thousand_char_description + "1")
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None
    
    # veryfying Condition FFTT error
    def test_create_product_18(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0wq@test.com")
        self.type("#title", "")
        self.type("#price", 10)
        self.type("#description", two_thousand_char_description)
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None
    
    # veryfying Condition FTFF error
    def test_create_product_19(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0wq@test.com")
        self.type("#title", "HELLO")
        self.type("#price", 9)
        self.type("#description", two_thousand_char_description + "1")
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="HELLO").first()
        assert new_prod is None
    
    # veryfying Condition FTFT error
    def test_create_product_20(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0wq@test.com")
        self.type("#title", "HELLO")
        self.type("#price", 9)
        self.type("#description", two_thousand_char_description)
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="HELLO").first()
        assert new_prod is None
    
    # veryfying Condition FTTF error
    def test_create_product_21(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0wq@test.com")
        self.type("#title", "HELLO")
        self.type("#price", 10)
        self.type("#description", two_thousand_char_description + "1")
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="HELLO").first()
        assert new_prod is None
    
    # veryfying Condition FTTT error
    def test_create_product_22(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0wq@test.com")
        self.type("#title", "HELLO")
        self.type("#price", 10)
        self.type("#description", two_thousand_char_description)
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="HELLO").first()
        assert new_prod is None
    
    # veryfying Condition TFFF error
    def test_create_product_23(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "")
        self.type("#price", 9)
        self.type("#description", two_thousand_char_description + "1")
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None
    
    # veryfying Condition TFFT error
    def test_create_product_24(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "")
        self.type("#price", 10)
        self.type("#description", two_thousand_char_description + "1")
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None

    # veryfying Condition TFTF error
    def test_create_product_25(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "")
        self.type("#price", 10)
        self.type("#description", two_thousand_char_description + "1")
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None
    
    # veryfying Condition TFTT error
    def test_create_product_26(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "")
        self.type("#price", 10)
        self.type("#description", two_thousand_char_description)
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None
    
    # veryfying Condition TTFF error
    def test_create_product_27(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "HI")
        self.type("#price", 9)
        self.type("#description", two_thousand_char_description + "1")
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="HI").first()
        assert new_prod is None
    
    # veryfying Condition TTFT error
    def test_create_product_28(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "GGEZ")
        self.type("#price", 0)
        self.type("#description", two_thousand_char_description)
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="GGEZ").first()
        assert new_prod is None
    
    # veryfying Condition TTTF error
    def test_create_product_29(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "GGEZ")
        self.type("#price", 10)
        self.type("#description", two_thousand_char_description + "1")
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="GGEZ").first()
        assert new_prod is None
    
    # veryfying Condition TTTT SUCCESS!!!
    def test_create_product_30(self, *_):
        self.open(base_url + '/createproduct')
        self.type("#user_email", "test0@test.com")
        self.type("#title", "GGEZ")
        self.type("#price", 10)
        self.type("#description", two_thousand_char_description)
        self.find_element("#Save").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="GGEZ").first()
        assert new_prod is not None
