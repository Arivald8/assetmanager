from selenium import webdriver
import unittest

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
        self.assertIn("Sign In", self.browser.title)

    def test_can_sign_up_for_an_account(self):
        # User navigates to the sign up url
        self.browser.get("http://localhost:8000/signUp/")
        # User notices the Sign Up form
        self.browser.find_element_by_id("signup_form")


if __name__ == "__main__":
    unittest.main(warnings="ignore")