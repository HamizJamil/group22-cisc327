from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from qbay.models import Product


two_thousand_char_description = ("111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "111111111111111111111111111111111111111111" +
                                 "11111111111111111111111111")
bad_title = ("111111111111111111111111111111111111111111111111111111" +
             "11111111111111111111111112")


class FrontEndProductUpdateTest(BaseCase):

    # SMOKE TESTS FOR CREATE PRODUCT
    # checking if submit and fill works
    def test_update_prod_1(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')  # open up the page
        self.type("#email", "test0@test.com")  # insert the text fields
        self.type("#title", "Iphone 11 Max Pro")
        self.type("#new_title", "Iphone 11 Mini Pro")
        self.type("#new_price", 1000)
        self.type("#new_description", "Brand-New, good and fast")
        self.find_element("#Submit").click()  # click save to submit
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="Iphone 11 Mini Pro").first()
        assert new_prod is not None

    # BOUNDARY TESTS FOR CREATE PRODUCT
    #  Checking when character title length is 1 char
    def test_update_prod_2(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Iphone 11 Mini Pro")
        self.type("#new_title", "12")
        self.type("#new_price", 1000)
        self.type("#new_description", "You wish your phone was this good")
        self.find_element("#Submit").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="12").first()
        assert new_prod is not None

    # checking when title length is 80 char
    def test_update_prod_3(self, *_):
        global bad_title
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "12")
        self.type("#new_title", bad_title)
        self.type("#new_price", 1000)
        self.type("#new_description", "11111111111111111111111" +
                  "111111111111111111" +
                  "1111111111111111111111111111111111111111")
        self.find_element("#Submit").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title=bad_title).first()
        assert new_prod is not None

    # veryfying error when description is 20 char long
    def test_update_prod_4(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", bad_title)
        self.type("#new_title", "Test4")
        self.type("#new_price", 1000)
        self.type("#new_description", "a2345678910111213141")
        self.find_element("#Submit").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="Test4").first()
        assert new_prod is not None

    # veryfying error when description is 2000 char long
    def test_update_prod_5(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test4")
        self.type("#new_title", "Test5u")
        self.type("#new_price", 1000)
        self.type("#new_description", two_thousand_char_description)
        self.find_element("#Submit").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="Test5u").first()
        assert new_prod is not None

    # verfifying not allowing lowering price
    def test_update_prod_6(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test5u")
        self.type("#new_title", "test6u")
        self.type("#new_price", 999)
        self.type("#new_description", "You wish your phone was this good")
        self.find_element("#Submit").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="test6u").first()
        assert new_prod is None

    # verfifying update of product when price $10000
    def test_update_prod_7(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test5u")
        self.type("#new_title", "Test7u")
        self.type("#new_price", 10000)
        self.type("#new_description", "You wish your phone was this good")
        self.find_element("#Submit").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="Test7u").first()
        assert new_prod is not None

    #  Checking when character title length is 0 char
    def test_update_prod_8(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "")
        self.type("#new_price", 1000)
        self.type("#new_description", "You wish your phone was this good")
        self.find_element("#Submit").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None

    #  Checking when character title length is 81 char
    def test_update_prod_9(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        bad_title = ("111111111111111111111111111111111111111111111111111111" +
                     "111111111111111111111111112")
        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", bad_title)
        self.type("#new_price", 10000)
        self.type("#new_description", "You wish your phone was this good")
        self.find_element("#Submit").click()
        # verifying a product is successfully commited
        new_prod = Product.query.filter_by(title=bad_title).first()
        assert new_prod is None

    # veryfying error when description is 19 char long
    def test_update_prod_10(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "Test11")
        self.type("#new_price", 1000)
        self.type("#new_description", "1234567891011121314")
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="Test11").first()
        assert new_prod is None

    #  Checking when character description length is 2001 char
    def test_update_prod_11(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        global two_thousand_char_description
        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "69")
        self.type("#new_price", 10000)
        self.type("#new_description", "a" +
                  two_thousand_char_description + "1")
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="69").first()
        assert new_prod is None

    # veryfying error when price is 9
    def test_update_prod_12(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "Test12u")
        self.type("#new_price", 9)
        self.type("#new_description", "Description Valid")
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="Test12u").first()
        assert new_prod is None

    # veryfying error when price is 10001
    def test_update_prod_13(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "Test14")
        self.type("#new_price", 10001)
        self.type("#new_description", "Description Valid")
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="Test14").first()
        assert new_prod is None

    # veryfying Condition FFFF error
    def test_update_prod_14(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0wq@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "")
        self.type("#new_price", 9)
        self.type("#new_description", two_thousand_char_description + "1")
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None

    # veryfying Condition FFFT error
    def test_update_prod_15(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0wq@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "")
        self.type("#new_price", 9)
        self.type("#new_description", two_thousand_char_description)
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None

    # veryfying Condition FFTF error
    def test_update_prod_16(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0wq@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "")
        self.type("#new_price", 10)
        self.type("#new_description", two_thousand_char_description + "1")
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None

    # veryfying Condition FFTT error
    def test_update_prod_17(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0wq@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "")
        self.type("#new_price", 10)
        self.type("#new_description", two_thousand_char_description)
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None

    # veryfying Condition FTFF error
    def test_update_prod_18(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0wq@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "HELLO")
        self.type("#new_price", 9)
        self.type("#new_description", two_thousand_char_description + "1")
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="HELLO").first()
        assert new_prod is None

    # veryfying Condition FTFT error
    def test_update_prod_19(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0wq@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "HELLO")
        self.type("#new_price", 9)
        self.type("#new_description", two_thousand_char_description)
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="HELLO").first()
        assert new_prod is None

    # veryfying Condition FTTF error
    def test_update_prod_20(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0wq@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "HELLO")
        self.type("#new_price", 10)
        self.type("#new_description", two_thousand_char_description + "1")
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="HELLO").first()
        assert new_prod is None

    # veryfying Condition FTTT error
    def test_update_prod_21(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0wq@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "HELLO")
        self.type("#new_price", 10)
        self.type("#new_description", two_thousand_char_description)
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="HELLO").first()
        assert new_prod is None

    # veryfying Condition TFFF error
    def test_update_prod_22(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "")
        self.type("#new_price", 9)
        self.type("#new_description", two_thousand_char_description + "1")
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None

    # veryfying Condition TFFT error
    def test_update_prod_23(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "")
        self.type("#new_price", 10)
        self.type("#new_description", two_thousand_char_description + "1")
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None

    # veryfying Condition TFTF error
    def test_update_prod_24(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "")
        self.type("#new_price", 10)
        self.type("#new_description", two_thousand_char_description + "1")
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None

    # veryfying Condition TFTT error
    def test_update_prod_25(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "")
        self.type("#new_price", 10)
        self.type("#new_description", two_thousand_char_description)
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="").first()
        assert new_prod is None

    # veryfying Condition TTFF error
    def test_update_prod_26(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "HI")
        self.type("#new_price", 9)
        self.type("#new_description", two_thousand_char_description + "1")
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="HI").first()
        assert new_prod is None

    # veryfying Condition TTFT error
    def test_update_prod_27(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "GGGG")
        self.type("#new_price", 0)
        self.type("#new_description", two_thousand_char_description)
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="GGGG").first()
        assert new_prod is None

    # veryfying Condition TTTF error
    def test_update_prod_28(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login

        self.open(base_url + '/updateproduct')
        self.type("#email", "test0@test.com")
        self.type("#title", "Test7u")
        self.type("#new_title", "GGGG")
        self.type("#new_price", 10)
        self.type("#new_description", two_thousand_char_description + "1")
        self.find_element("#Submit").click()
        # verifying a product is NOT successfully commited
        new_prod = Product.query.filter_by(title="GGGG").first()
        assert new_prod is None
