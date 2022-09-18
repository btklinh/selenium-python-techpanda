import pytest
from pages.Home_Page import HomePage
from utilities.utils import random_email

@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.home = HomePage(self.driver)

    def test_01_login_success(self):
        self.home.click_on_account_menu()
        login = self.home.click_on_login_link()
        login.input_email("btklinh999@gmail.com")
        login.input_password("11111111")
        my_acc = login.click_login_button()
        assert my_acc.get_account_name_header() == ("WELCOME, AAAA AAAA!")

    def test_02_login_incorrect_email(self):
        self.home.click_on_account_menu()
        login = self.home.click_on_login_link()
        login.input_email("dfaweff@gmail.com")
        login.input_password("11111111")
        login.click_login_button()
        assert login.get_error_message() == ("Invalid login or password.")

    def test_03_login_incorrect_password(self):
        self.home.click_on_account_menu()
        login = self.home.click_on_login_link()
        login.input_email("btklinh999@gmail.com")
        login.input_password("abcd1234")
        login.click_login_button()
        assert login.get_error_message() == ("Invalid login or password.")

    def test_04_login_email_blank(self):
        self.home.click_on_account_menu()
        login = self.home.click_on_login_link()
        login.input_email("")
        login.input_password("11111111")
        login.click_login_button()
        assert login.get_error_message_email_blank() == ("This is a required field.")

    def test_05_login_password_blank(self):
        self.home.click_on_account_menu()
        login = self.home.click_on_login_link()
        login.input_email("btklinh999@gmail.com")
        login.input_password("")
        login.click_login_button()
        assert login.get_error_message_password_blank() == ("This is a required field.")