from decouple import config as cfg

import firebase_admin
from firebase_admin import auth
import pyrebase


class Authenticator:
    """
    Authenticator:
        Used to create authenticator objects which take care of 
        Django to Firebase authentication of users.

        Objects of Authenticator can be used to:
            * Check user claims
            * Allow access to any given resource
            * Deny access to any given resource

        Methods of Authenticator can:
            * Sign in a user
            * Sign out a user
            * Create a user
            * Delete a user
            * Edit user claims:
                * Add Claim
                * Delete Claim 
    """
    def __init__(
        self,
        user_obj = None, 
        default_app = firebase_admin.initialize_app(firebase_admin.credentials.Certificate(f"{cfg('GOOGLE_CREDENTIALS')}")), 
        firebase = pyrebase.initialize_app(
            {
            "apiKey": cfg('FIREBASE_apiKey'),
            "authDomain": cfg('FIREBASE_authDomain'),
            "projectId": cfg('FIREBASE_projectId'),
            "storageBucket": cfg('FIREBASE_storageBucket'),
            "messagingSenderId": cfg('FIREBASE_messagingSenderId'),
            "appId": cfg('FIREBASE_appId'),
            "databaseURL": "NONE",
            "measurementId": cfg('FIREBASE_measurementId')
            }
        ),
        authe = None
        ):

        self.user_obj = user_obj
        self.default_app = default_app
        self.firebase = firebase
        self.authe = self.firebase.auth()


    def __str__(self):
        if self.user_obj['registered'] != '':
            return str(f"Authenticator contains:{self.user_obj['email']}")
        else:
            return str(f"Authenticator objects contains an unregistered user.")

    def __repr__(self):
        return str(f"""
            Authenticator contains:\n
            localId: {self.user_obj['localId']}\n
            email: {self.user_obj['email']}\n
            displayName: {self.user_obj['displayName']}\n
            idToken: {self.user_obj['idToken']}\n
            registered: {self.user_obj['registered']}\n
            refreshToken: {self.user_obj['refreshToken']}\n
            expiredIn: {self.user_obj['expiresIn']}
        """)

    def user_sign_in(self, request):
        try:
            user = self.authe.sign_in_with_email_and_password(
                request.POST.get('email'), 
                request.POST.get('pass')
            )
            pass
        except:
            return [request, "login.html", {"message": "Invalid Credentials..."}]
        request.session['idToken'] = str(user['idToken'])
        request.session['uid'] = str(user['localId'])
        return [request, "index.html", {"request_keys": [_ for _ in request.session.items()]}]


    def user_sign_up(self, request):
        try:
            user = auth.create_user(
                email=request.POST.get('email'),
                password=request.POST.get('pass')
            )
        except:
            return [request, "registration.html"]
        return [request, "login.html"]