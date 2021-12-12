from django.http import JsonResponse

from decouple import config as cfg

import firebase_admin
from firebase_admin import auth
import pyrebase


class Authenticator:
    """
    Authenticator:
        Takes care of 
        Django to Firebase authentication of users.

        Authenticator can be used to:
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
        if self.user_obj is not None:
            if self.user_obj['registered'] != '':
                return str(f"Authenticator contains:{self.user_obj['email']}")
            else:
                return str(f"Authenticator object contains an unregistered user.")
        else:
            return str(self.user_obj)


    def __repr__(self):
        if self.user_obj is not None:
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
        else:
            return str(f"Authenticator object contains an unregistered user.")


    def access_denied(self):
        return ["index.html", {"unauthorized": "Access Denied"}]


    def is_admin(self, request):
        try:
            claims = auth.verify_id_token(request.COOKIES['idToken'])
            try:
                if claims['admin'] is True:
                    return True
                else:
                    return False
            except:
                return False
        except:
            return False


    def is_school_lead(self, request):
        try:
            claims = auth.verify_id_token(request.COOKIES['idToken'])
            try:
                if claims['school_lead'] is True:
                    return True
                else:
                    return False
            except:
                return False
        except:
            return False


    def is_technician(self, request):
        try:
            claims = auth.verify_id_token(request.COOKIES['idToken'])
            try:
                if claims['technician'] is True:
                    return True
                else:
                    return False
            except:
                return False
        except:
            return False


    def is_staff(self, request):
        try:
            claims = auth.verify_id_token(request.COOKIES['idToken'])
            try:
                if claims['staff'] is True:
                    return True
                else:
                    return False
            except:
                return False
        except:
            return False

    
    def user_permissions_generic_elevated(self, request):
        """ 
        Returns a list of generic elevated permissions of the user.

        This method can be used to check whether a user has generic
        elevated permissions, ie. user is not just a staff member.
        """
        return [
            self.is_admin(request),
            self.is_school_lead(request),
            self.is_technician(request),
        ]

    
    def user_permissions_specific(self, request):
        """
        Returns a dictionary of user permissions,
        specifying all roles.

        This method can be used to check if a user
        has any of the specific permissions.
        """
        return {
            "admin": self.is_admin(request),
            "school_lead": self.is_school_lead(request),
            "technician": self.is_technician(request),
            "staff": self.is_staff(request)
        }


    def user_sign_in(self, request):
        try:
            user = self.authe.sign_in_with_email_and_password(
                request.POST.get('email'), 
                request.POST.get('pass')
            )
            pass
        except Exception as e:
            return JsonResponse({"Error": "Invalid Credentials..."})
        server_response = JsonResponse({
            'idToken': str(user['idToken']),
            'uid': str(user['localId']),
            'user': request.POST.get('email')
        })

        server_response.set_cookie(
                key='idToken', 
                value=str(user['idToken']),
                httponly=True,
                samesite='Lax'
            )
        server_response.set_cookie(
                key='uid', 
                value=str(user['localId']),
                httponly=False,
                samesite='Lax'
            )
        return server_response

    def user_sign_up(self, request):
        try:
            user = auth.create_user(
                email=request.POST.get('email'),
                password=request.POST.get('pass')
            )
            auth.set_custom_user_claims(user['localId'],
            {
                'admin': False,
                'school_lead': False,
                'technician': False,
                'staff': False,
            })
        except:
            return [request, "registration.html"]
        return [request, "login.html"]


    def user_logout(self, request):
        try:
            print("debug here")

            response = JsonResponse({
                "Success": "You have been successfully signed out."
            })

            response.delete_cookie('idToken')
            response.delete_cookie('uid')
            return response
        except Exception as e:
            print(e)
            response = JsonResponse({
                "Error": "We were unable to sign you out at this time. Please try again."
            })
            print("debug not work")
            return response
    
    def return_user_claims(self, user_email):
        return auth.get_user_by_email(user_email).custom_claims



    def check_user_claims(self, request):
        try:
            claims = auth.verify_id_token(request.session['idToken'])
            print(claims)
        except Exception as e:
            print(e)
            pass


    def add_user_claims(self, request):
        try:
            user = auth.get_user_by_email(request.POST.get('user_email'))
            user_claims = user.custom_claims

            if request.POST.get('admin_claim') == 'on':
                user_claims.update({'admin': True})

            if request.POST.get('school_lead_claim') == 'on':
                user_claims.update({'school_lead': True})


            if request.POST.get('technician_claim') == 'on':
                user_claims.update({'technician': True})

            if request.POST.get('staff_claim') == 'on':
                user_claims.update({'staff': True})

            auth.set_custom_user_claims(user.uid, user_claims)
        except Exception as e:
            return [request, "admins.html", {'e': e}]
        return [request, "admins.html", {'Success': 'Claims added successfully!'}]