from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import Product
from selenium import webdriver

from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import Product
from selenium import webdriver


class FrontEndLoginTest(BaseCase):
    
    # STATE TRANSITION TESTS FOR LOGIN
    # Checking if login button works and routes correctly
    # User should be logged in, proper credentials provided
    def test_login_1(self, *_):
        self.open(base_url + '/login')  # open up the page
        self.type("#user_email", "test0@test.com")  # insert the text fields
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to homepage
        self.assert_title("Home Page")  

    # Verifying false credentials re-route user properly
    # No user should be logged in
    def test_login_2(self, *_):
        self.open(base_url + '/login')
        self.type("#user_email", "test0@test.com")
        self.type("#user_pass", "wrongPasswordLOL")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")  

    # OUTPUT PARTITION TESTING FOR LOGIN
    #  User not successfully logged in 
    #  As a cause of empty email input
    def test_login_3(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "")
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")  

    # User not successfully logged in
    # As a cause of empty password input
    def test_login_4(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0@test.com")
        self.type("#user_pass", "")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")  

    # User not successfully logged in
    # As a cause of wrong email input
    def test_login_5(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0test")
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")  
    
    # User not successfully logged in
    # As a cause of wrong email input
    def test_login_6(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0test@test")
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")  

    # User not successfully logged in
    # As a cause of wrong email input
    def test_login_7(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0#$%@test.com")
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")  
    
    # User not successfully logged in
    # As a cause of password missing uppercase character
    def test_login_8(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0@test.com")
        self.type("#user_pass", "e123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")  
    
    # User not successfully logged in
    # As a cause of password missing lowercase character
    def test_login_9(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0@test.com")
        self.type("#user_pass", "A123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")
        self.assert_element('#alert')  

    # User is successfully logged in
    def test_login_10(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0@test.com")
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Home Page")

    # INPUT PARTITION TESTING
    # Input has an empty email address
    def test_login_11(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", " ")
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")
        self.assert_element('#alert')

    # Input has missing @ in email address
    def test_login_12(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0.com")
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")

    # Input has missing .com/.ca in email address
    def test_login_13(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0@")
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")

    # Input has special characters in email address
    def test_login_14(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0!$%@test.com")
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")
        self.assert_element('#alert')

    # Input has missing password
    def test_login_15(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0@test.com")
        self.type("#user_pass", "")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")
        self.assert_element('#alert')

    # Input has password with less than 6 characters
    def test_login_16(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0@test.com")
        self.type("#user_pass", "eA12!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")
        self.assert_element('#alert')
    
    # Input has password with no uppercase character
    def test_login_17(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0@test.com")
        self.type("#user_pass", "e123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")
        self.assert_element('#alert')
    
    # Input has password with no lowercase character
    def test_login_18(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0@test.com")
        self.type("#user_pass", "A123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")
        self.assert_element('#alert')
    
    # Input has password with no special characters
    def test_login_19(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0@test.com")
        self.type("#user_pass", "eA123456")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")
        self.assert_element('#alert')

    # Input's password does not match email registered
    def test_login_20(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0@test.com")
        self.type("#user_pass", "WrongPassword123!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")

    # Input's email does not match password registered
    def test_login_21(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test5@test.com")
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")
    
    # Input's email is not registered, user doesnt exist
    def test_login_22(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "fail0@test.com")
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Login page
        self.assert_title("Login")

    # Input satisfies email and password requirements
    def test_login_23(self, *_):  
        self.open(base_url + '/login')
        self.type("#user_email", "test0@test.com")
        self.type("#user_pass", "eA123456!")
        self.find_element("#login").click()  # click login to submit
        # verifying that it redirects to Home Page
        self.assert_title("Home Page")
    
    