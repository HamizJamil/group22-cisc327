from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from qbay.models import User
from cryptography import fernet


class FrontEndProductUpdateTest(BaseCase):

    # SMOKE TEST FOR REGISTER
    # check if submit and fill works
    def test_register_1(self, *_):
        new_user = None
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "john123")  # insert the text fields
        self.type("#user_email", "john123@test.com")
        self.type("#user_pass", "John123!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying successful registration
        new_user = User.query.filter_by(email="john123@test.com").first()
        assert new_user is not None

    # OUTPUT PARTITIONING TEST
    # empty email
    def test_register_2(self, *_):

        new_user = None
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "john1234")  # insert the text fields
        self.type("#user_email", "")
        self.type("#user_pass", "John123!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user isn't made
        new_user = User.query.filter_by(user_name="john1234").first()
        assert new_user is None

    # empty password
    def test_register_3(self, *_):

        new_user = None
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "john12345")  # insert the text fields
        self.type("#user_email", "john1234@gmail.com")
        self.type("#user_pass", "")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user isn't made
        new_user = User.query.filter_by(user_name="john12345").first()
        assert new_user is None

    # check email format
    def test_register_4(self, *_):

        new_user = None
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "john12346")  # insert the text fields
        self.type("#user_email", "john1234")
        self.type("#user_pass", "John123!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user isn't made
        new_user = User.query.filter_by(user_name="john12346").first()
        assert new_user is None

    # password less than 6 char
    def test_register_5(self, *_):

        new_user = None
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "john12346")  # insert the text fields
        self.type("#user_email", "john1234@gmail.com")
        self.type("#user_pass", "Joh1!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user isn't made
        new_user = User.query.filter_by(user_name="john12346").first()
        assert new_user is None

    # password has no special char
    def test_register_6(self, *_):

        new_user = None
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "john12346")  # insert the text fields
        self.type("#user_email", "john1234@gmail.com")
        self.type("#user_pass", "John123")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user isn't made
        new_user = User.query.filter_by(user_name="john12346").first()
        assert new_user is None

    # password has no lower case
    def test_register_7(self, *_):

        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "john12346")  # insert the text fields
        self.type("#user_email", "john1234@gmail.com")
        self.type("#user_pass", "JOHN123!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user isn't made
        new_user = User.query.filter_by(user_name="john12346").first()
        assert new_user is None

    # username is empty
    def test_register_8(self, *_):

        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "")  # insert the text fields
        self.type("#user_email", "john1234@gmail.com")
        self.type("#user_pass", "John123!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user isn't made
        new_user = User.query.filter_by(user_name="").first()
        assert new_user is None

    # username is not alphanumeric only
    def test_register_9(self, *_):
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "john12346!")  # insert the text fields
        self.type("#user_email", "john1234@gmail.com")
        self.type("#user_pass", "John123!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user isn't made
        new_user = User.query.filter_by(user_name="john12346!").first()
        assert new_user is None

    # username has space at suffix
    def test_register_10(self, *_):
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "john12346 ")  # insert the text fields
        self.type("#user_email", "john1234@gmail.com")
        self.type("#user_pass", "John123!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user isn't made
        new_user = User.query.filter_by(user_name="john12346 ").first()
        assert new_user is None

    # username has space at prefix
    def test_register_11(self, *_):
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", " john12346")  # insert the text fields
        self.type("#user_email", "john1234@gmail.com")
        self.type("#user_pass", "John123!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user isn't made
        new_user = User.query.filter_by(user_name=" john12346").first()
        assert new_user is None

    # username longer than 20 char
    def test_register_12(self, *_):
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "john1234678910111213555")  # insert text field
        self.type("#user_email", "john1234@gmail.com")
        self.type("#user_pass", "John123!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user isn't made
        new_user = User.query.filter_by(user_name="john1234678" +
                                                  "910111213555").first()
        assert new_user is None

    # username less than 3 char
    new_user = None

    def test_register_13(self, *_):
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "j")  # insert the text fields
        self.type("#user_email", "john1234@gmail.com")
        self.type("#user_pass", "John123!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user isn't made
        new_user = User.query.filter_by(user_name="j").first()
        assert new_user is None

    # repeated email
    def test_register_14(self, *_):
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "john1234567")  # insert the text fields
        self.type("#user_email", "john123@test.com")
        self.type("#user_pass", "John123!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying successful registration
        new_user = User.query.filter_by(user_name="john1234567").first()
        assert new_user is None

    # BOUNDARY TESTS
    # 19 character username
    def test_register_15(self, *_):
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "john123456789123456")  # insert the text field
        self.type("#user_email", "john1234@gmail.com")
        self.type("#user_pass", "John123!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user is made
        new_user = User.query.filter_by(user_name="john12345678" +
                                                  "9123456").first()
        assert new_user is not None

    # 3 character username
    def test_register_16(self, *_):
        self.open(base_url + '/registration')  # open up the page
        self.type("#user_name", "jo3")  # insert the text fields
        self.type("#user_email", "john12345@gmail.com")
        self.type("#user_pass", "John123!")
        self.find_element("#Submit").click()  # click save to submit
        # verifying user is made
        new_user = User.query.filter_by(user_name="jo3").first()
        assert new_user is not None
