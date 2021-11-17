from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_can_navigate_to_home_page(self):
        # User navigates to the to the home page of the web app
        self.browser.get("http://localhost:8000")
        # User notices the page title
        assert "WISF Asset Manager" in self.browser.title

if __name__ == "__main__":
    unittest.main(warnings="ignore")