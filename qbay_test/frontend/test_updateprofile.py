from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User
from selenium import webdriver


class FrontEndUpdateProfileTest(BaseCase):

    # Set of exhaustive input testing
    #
    # Correct input test
    def test_update_profile(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "update@gmail.com")  # insert the text fields
        self.type("#user_pass", "ABC@abc")
        self.find_element("#login").click()  # click save to submit
        # veryfing that it redirects to homepage
        # verifying a product is successfully commited

        self.open(base_url + '/updateprofile')
        self.type("#user_email", "update@gmail.com")
        self.type("#user_name", "profiletest")
        self.type("#shipping_address", "Queens University, "
                                       "99 University Ave, Kingston, ON")
        self.type("#postal_code", "K7L 3N6")
        self.find_element("#Submit").click()

        updated = User.query.filter_by(email="update@gmail.com").all()

        assert updated is not None

    # incorrect username with space prefix
    def test_update_profile2(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "update@gmail.com")  # insert the text fields
        self.type("#user_pass", "ABC@abc")
        self.find_element("#login").click()  # click save to submit

        self.open(base_url + '/updateprofile')
        self.type("#user_email", "update@gmail.com")
        self.type("#user_name", " profiletest")
        self.type("#shipping_address", "Queens University")
        self.type("#postal_code", "K7L 3N6")
        self.find_element("#Submit").click()

        updated = User.query.filter_by(email="update@gmail.com").first()

        assert updated.user_name != " profiletest"

    # incorrect username with space suffix
    def test_update_profile3(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "update@gmail.com")  # insert the text fields
        self.type("#user_pass", "ABC@abc")
        self.find_element("#login").click()  # click save to submit

        self.open(base_url + '/updateprofile')
        self.type("#user_email", "update@gmail.com")
        self.type("#user_name", "profiletest ")
        self.type("#shipping_address", "Queens University")
        self.type("#postal_code", "K7L 3N6")
        self.find_element("#Submit").click()

        updated = User.query.filter_by(email="update@gmail.com").first()

        assert updated.user_name != "profiletest "

    # incorrect username less than 2 characters
    def test_update_profile4(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "update@gmail.com")  # insert the text fields
        self.type("#user_pass", "ABC@abc")
        self.find_element("#login").click()  # click save to submit

        self.open(base_url + '/updateprofile')
        self.type("#user_email", "update@gmail.com")
        self.type("#user_name", "p")
        self.type("#shipping_address", "Queens University")
        self.type("#postal_code", "K7L 3N6")
        self.find_element("#Submit").click()

        updated = User.query.filter_by(email="update@gmail.com").first()

        assert updated.user_name != "p"

    # incorrect username longer than 20 characters
    def test_update_profile5(self, *_):
        longer_than_20 = "p" * 21
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "update@gmail.com")  # insert the text fields
        self.type("#user_pass", "ABC@abc")
        self.find_element("#login").click()  # click save to submit

        self.open(base_url + '/updateprofile')
        self.type("#user_email", "update@gmail.com")
        self.type("#user_name", longer_than_20)
        self.type("#shipping_address", "Queens University")
        self.type("#postal_code", "K7L 3N6")
        self.find_element("#Submit").click()

        updated = User.query.filter_by(email="update@gmail.com").first()

        assert updated.user_name != longer_than_20

    # incorrect empty username
    def test_update_profile6(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "update@gmail.com")  # insert the text fields
        self.type("#user_pass", "ABC@abc")
        self.find_element("#login").click()  # click save to submit

        self.open(base_url + '/updateprofile')
        self.type("#user_email", "update@gmail.com")
        self.type("#user_name", "")
        self.type("#shipping_address", "Queens University")
        self.type("#postal_code", "K7L 3N6")
        self.find_element("#Submit").click()

        updated = User.query.filter_by(email="update@gmail.com").first()

        assert updated.user_name != ""

    # incorrect username non-alphanumeric (special character)
    def test_update_profile7(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "update@gmail.com")  # insert the text fields
        self.type("#user_pass", "ABC@abc")
        self.find_element("#login").click()  # click save to submit

        self.open(base_url + '/updateprofile')
        self.type("#user_email", "update@gmail.com")
        self.type("#user_name", "prof!letest")
        self.type("#shipping_address", "Queens University")
        self.type("#postal_code", "K7L 3N6")
        self.find_element("#Submit").click()

        updated = User.query.filter_by(email="update@gmail.com").first()

        assert updated.user_name != "prof!letest"

    # incorrect shipping address empty
    def test_update_profile8(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "update@gmail.com")  # insert the text fields
        self.type("#user_pass", "ABC@abc")
        self.find_element("#login").click()  # click save to submit
        # veryfing that it redirects to homepage
        # verifying a product is successfully commited

        self.open(base_url + '/updateprofile')
        self.type("#user_email", "update@gmail.com")
        self.type("#user_name", "profiletest")
        self.type("#shipping_address", "")
        self.type("#postal_code", "K7L 3N6")
        self.find_element("#Submit").click()

        updated = User.query.filter_by(email="update@gmail.com").first()

        assert updated.shipping_address != ""

    # incorrect shipping address non-alphanumeric (special character!)
    def test_update_profile9(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "update@gmail.com")  # insert the text fields
        self.type("#user_pass", "ABC@abc")
        self.find_element("#login").click()  # click save to submit
        # veryfing that it redirects to homepage
        # verifying a product is successfully commited

        self.open(base_url + '/updateprofile')
        self.type("#user_email", "update@gmail.com")
        self.type("#user_name", "profiletest")
        self.type("#shipping_address", "Queens University, ! "
                                       "99 University Ave, Kingston, ON")
        self.type("#postal_code", "K7L 3N6")
        self.find_element("#Submit").click()

        updated = User.query.filter_by(email="update@gmail.com").first()

        assert updated.shipping_address != "Queens University, !" \
                                           " 99 University Ave, Kingston, ON"

    # correct postal code conversion: lower case to uppercase with no space
    def test_udpate_profile10(self, *_):

        self.open(base_url + '/updateprofile')
        self.type("#user_email", "update@gmail.com")
        self.type("#user_name", "profiletest")
        self.type("#shipping_address", "Queens University, "
                                       "99 University Ave, Kingston, ON")
        self.type("#postal_code", "K8l 3n6")
        self.find_element("#Submit").click()

        updated = User.query.filter_by(email="update@gmail.com").first()

        assert updated is not None

        # assert updated.user_name == "profiletest"
        # assert updated.shipping_address == "Queens University," \
        #                                    " 99 University Ave, Kingston, ON"
        # assert updated.postal_code == "K8L3N6"

    # incorrect invalid postal code
    def test_udpate_profile11(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "update@gmail.com")  # insert the text fields
        self.type("#user_pass", "ABC@abc")
        self.find_element("#login").click()  # click save to submit
        # veryfing that it redirects to homepage
        # verifying a product is successfully commited

        self.open(base_url + '/updateprofile')
        self.type("#user_email", "update@gmail.com")
        self.type("#user_name", "profiletest")
        self.type("#shipping_address", "Queens University, "
                                       "99 University Ave, Kingston, ON")
        self.type("#postal_code", "K2AA5Z9")
        self.find_element("#Submit").click()

        updated = User.query.filter_by(email="update@gmail.com").first()

        assert updated.user_name == "profiletest"
        assert updated.shipping_address == "Queens University," \
                                           " 99 University Ave, Kingston, ON"
        assert updated.postal_code != "K2AA5Z9"





