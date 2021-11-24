from django.urls import resolve
from django.test import TestCase
from decouple import config as cfg
from assetmanager.views import home_page
from assetmanager.authenticator import Authenticator


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


class AuthenticatorTest(TestCase):
    def test_object_initialization(self):
        auth = Authenticator()
        self.assertEqual(auth.user_obj, None)
        #self.assertEqual(auth.)
        # Write rest of the tests here

    
    def test_string_representation(self):
        # User object has been initialized
        # but the user is not registered
        self.assertEqual(
            "Authenticator objects contains an unregistered user.",
            Authenticator().__str__()
        )
        # User object has not been initialized
        self.assertEqual(
            "None",
            Authenticator().__str__()
        )
        # User object has been initialized
        # and user is registered
        self.assertEqual(
            "Authenticator contains:",
            Authenticator().__str__()
        )


    def test_repr_representation(self):
        # User object has been initialized
        self.assertIn(
            "Authenticator contains:",
            Authenticator().__repr__()
        )
        # User object has not been initialized
        self.assertIn(
            "Authenticator object contains",
            Authenticator().__repr__()
        )

    
    def test_access_denied_method(self):
        self.assertListEqual(
            ["index.html", {"unauthorized": "Access Denied"}],
            Authenticator().access_denied()
        )

        