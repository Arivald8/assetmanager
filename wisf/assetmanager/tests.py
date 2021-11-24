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
        
        sign_in_request = Authenticator().user_sign_in(request)
        self.assertTrue(sign_in_request[2]['request_keys'])

    
    def test_if_user_has_admin_claims(self):
        request = self.factory.get('addclaims/')
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.session['idToken'] = self.user['idToken']

        claims = fb_auth.verify_id_token(request.session['idToken'])
        print(claims['admin'])

        # User with admin claims
        self.assertTrue(Authenticator().is_admin(request))

        request.session['idToken'] = "None"

        # Anonymous user with no claims
        self.assertFalse(Authenticator().is_admin(request))
        

