from selenium import webdriver
import unittest
from decouple import config as cfg
from time import sleep


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_can_navigate_to_home_page(self):
        # User navigates to the home page of the web app
        self.browser.get("http://localhost:8000")
        # User notices the page title
        self.assertIn("WISF Asset Manager", self.browser.title)
        # User notices the welcome message
        self.browser.find_element_by_id("welcome_message")

    def test_can_sign_up_for_an_account(self):
        # User navigates to the sign up url
        self.browser.get("http://localhost:8000/signup/")
        # User notices the Sign Up form
        self.browser.find_element_by_id("signup_form")

        # User fills in the necessary information
        username = self.browser.find_element_by_id("Username")
        email = self.browser.find_element_by_id("Email")
        password = self.browser.find_element_by_id("Password")
        confirm_password = self.browser.find_element_by_id("confirm_password")

        username.send_keys(f"{cfg('TEST_USERNAME')}")
        sleep(2)
        email.send_keys(f"{cfg('TEST_EMAIL')}")
        sleep(2)
        password.send_keys(f"{cfg('TEST_PASSWORD')}")
        sleep(2)
        confirm_password.send_keys(f"{cfg('TEST_CONFIRM_PASSWORD')}")

        # User locates and clicks on the SignUp button
        signup_button = self.browser.find_element_by_id("signup_button")
        sleep(2)
        signup_button.click()

class ExistingUserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_can_log_in(self):
        # User navigates to the login page
        self.browser.get("http://localhost:8000/signin/")
        # User spots the login form
        self.browser.find_element_by_id("sign_in_form")

        # User fills in the necessary information
        email = self.browser.find_element_by_id("Email")
        password = self.browser.find_element_by_id("Password")

        email.send_keys(f"{cfg('TEST_EMAIL')}")
        sleep(2)
        password.send_keys(f"{cfg('TEST_PASSWORD')}")

        # User loocates and clicks on the sing in button
        signin_button = self.browser.find_element_by_id("signin_button")
        sleep(2)
        signin_button.click()


if __name__ == "__main__":
    unittest.main(warnings="ignore")