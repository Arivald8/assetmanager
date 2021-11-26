from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions import middleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import resolve
from django.test import TestCase
from django.test.client import RequestFactory

from decouple import config as cfg

from firebase_admin import auth as fb_auth

from assetmanager.views import home_page
from assetmanager.authenticator import Authenticator

import random
import string


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


class AuthenticatorTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.auth = Authenticator()

        self.request = self.factory.post('signin/', {'email': cfg('TEST_EMAIL'), 'pass': cfg('TEST_PASSWORD')})
        self.middleware = SessionMiddleware()
        self.middleware.process_request(self.request)
        self.request.session.save()

    
    def test_access_denied_method(self):
        self.assertListEqual(
            ["index.html", {"unauthorized": "Access Denied"}],
            self.auth.access_denied()
        )

    
    def test_if_user_has_admin_claims(self):
        self.request = Authenticator().user_sign_in(self.request)[0]
        self.assertTrue(Authenticator().is_admin(self.request))


    def test_if_user_has_school_lead_claims(self):
        self.request = Authenticator().user_sign_in(self.request)[0]
        self.assertTrue(Authenticator().is_school_lead(self.request))


    def test_if_user_has_technician_claims(self):
        self.request = Authenticator().user_sign_in(self.request)[0]
        self.assertTrue(Authenticator().is_technician(self.request))


    def test_if_user_has_staff_claims(self):
        self.request = Authenticator().user_sign_in(self.request)[0]
        self.assertTrue(Authenticator().is_technician(self.request))


    def test_if_user_has_generic_elevated_permissions(self):
        self.request = Authenticator().user_sign_in(self.request)[0]
        self.assertIn(True, Authenticator().user_permissions_generic_elevated(self.request))


    def test_if_user_has_specific_permissions(self):
        self.request = Authenticator().user_sign_in(self.request)[0]
        self.assertEqual({
            "admin": True,
            "school_lead": True,
            "technician": True,
            "staff": True
        }, Authenticator().user_permissions_specific(self.request))


    def test_user_can_sign_in(self):
        self.request = Authenticator().user_sign_in(self.request)[0]
        self.assertTrue(self.request.session['idToken'])
        self.assertTrue(self.request.session['uid'])


    def test_user_can_sign_up(self):
        def random_email():
            return ''.join(random.choice(string.ascii_letters) for _ in range(8))

        signup_request = self.factory.post('signup/', {
            f"{random_email()}@testmail.com", cfg('TEST_PASSWORD')
        })
        self.middleware.process_request(signup_request)
        signup_request.session.save()

        self.assertEqual({
            "admin": False,
            "school_lead": False,
            "technician": False,
            "staff": False
        }, Authenticator().user_permissions_specific(signup_request))








    

        

