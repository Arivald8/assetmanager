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


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


class AuthenticatorTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.auth = Authenticator()

    
    def test_access_denied_method(self):
        self.assertListEqual(
            ["index.html", {"unauthorized": "Access Denied"}],
            self.auth.access_denied()
        )


    def test_user_can_sign_in(self):
        request = self.factory.post('signin/', {'email': cfg('TEST_EMAIL'), 'pass': cfg('TEST_PASSWORD')})
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        
        Authenticator().user_sign_in(request)
        self.assertTrue(request.session['idToken'])

    
    def test_if_user_has_admin_claims(self):
        request = self.factory.post('admindash/', {'email': cfg('TEST_EMAIL'), 'pass': cfg('TEST_PASSWORD')})
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        Authenticator().user_sign_in(request)

        fb_auth.verify_id_token(request.session['idToken'])
        # User with admin claims
        self.assertTrue(Authenticator().is_admin(request))

        

