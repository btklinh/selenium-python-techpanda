import pytest
from pages.Home_Page import HomePage
from utilities.utils import random_email


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    # @pytest.fixture
    # def class_setup(self):
    #     self.home = HomePage(self.driver)

    first_name = "bui"
    middle_name = "thi"
    last_name = "linh"
    random = random_email()
    email = random.create_random_email()
    password = "abcd1234"
    invalid_email = "test_123"


    # def test_create_account_first_name_blank(self):
    #     # 1. Open LiveGuru99 site
    #     # 2. Click on 'ACCOUNT' menu
    #     self.home.click_on_account_menu()
    #
    #     # 3. Choose 'Register' link
    #     create_acc = self.home.click_on_register_link()
    #
    #     # 4. Input blank data to form
    #     create_acc.input_first_name("")
    #     create_acc.input_middle_name(self.middle_name)
    #     create_acc.input_last_name(self.last_name)
    #     create_acc.input_email(self.email)
    #     create_acc.input_password(self.password)
    #     create_acc.input_confirm_password(self.password)
    #
    #     # 5. Click to 'REGISTER' button
    #     create_acc.click_register_button()
    #
    #     # 6. Verify text message displayed
    #     assert create_acc.error_message_displayed() == "This is a required field."

    # def test_create_account_invalid_email(self):
    #     # 2. Click on 'ACCOUNT' menu
    #     self.home.click_on_account_menu()
    #
    #     # 3. Choose 'Register' link
    #     create_acc = self.home.click_on_register_link()
    #
    #     # 4. Input blank data to form
    #     create_acc.input_first_name(self.first_name)
    #     create_acc.input_middle_name(self.middle_name)
    #     create_acc.input_last_name(self.last_name)
    #     create_acc.input_email(self.invalid_email)
    #     create_acc.input_password(self.password)
    #     create_acc.input_confirm_password(self.password)
    #
    #     # 5. Click to 'REGISTER' button
    #     create_acc.click_register_button()
    #
    #     # 6. Verify text message displayed
    #     assert create_acc.alert_popup_displayed() == "Please include an '@' in the email address. 'lynn22132' is missing an '@'"

    def test_create_account_success(self):
        self.home = HomePage(self.driver)
        # 1. Open LiveGuru99 site
        # 2. Click on 'ACCOUNT' menu
        self.home.click_on_account_menu()

        # 3. Choose 'Register' link
        create_acc = self.home.click_on_register_link()

        # 4. Input all valid data to form
        create_acc.input_first_name(self.first_name)
        create_acc.input_middle_name(self.middle_name)
        create_acc.input_last_name(self.last_name)
        create_acc.input_email(self.email)
        create_acc.input_password(self.password)
        create_acc.input_confirm_password(self.password)

        # 5. Click to 'REGISTER' button
        my_acc = create_acc.click_register_button()

        # 6. Verify text displayed after registered successfully
        assert my_acc.create_account_success_message() == "Thank you for registering with Main Website Store."
        assert my_acc.get_account_name_header() == ("WELCOME, " + self.first_name.upper() + " " +self.middle_name.upper() + " " + self.last_name.upper() + "!")

