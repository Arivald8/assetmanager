from django.shortcuts import render
from decouple import config as cfg

import firebase_admin
from firebase_admin import auth
import pyrebase

cred = firebase_admin.credentials.Certificate(f"{cfg('GOOGLE_CREDENTIALS')}")
default_app = firebase_admin.initialize_app(cred)

config={
    "apiKey": cfg('FIREBASE_apiKey'),
    "authDomain": cfg('FIREBASE_authDomain'),
    "projectId": cfg('FIREBASE_projectId'),
    "storageBucket": cfg('FIREBASE_storageBucket'),
    "messagingSenderId": cfg('FIREBASE_messagingSenderId'),
    "appId": cfg('FIREBASE_appId'),
    "databaseURL": "NONE",
    "measurementId": cfg('FIREBASE_measurementId')
}

# Initialising the above config
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()


def sign_in(request):
    return render(request, "login.html")

def post_sign_in(request):
    email = request.POST.get('email')
    password = request.POST.get('pass')

    try:
        # If there is no error, then sign in 
        # the user with provided credentials
        user = authe.sign_in_with_email_and_password(email, password)
        pass
    except:
        message = "Invalid Credentials..."
        return render(request, "login.html", {"message": message})

    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    request_keys = [_ for _ in request.session.items()]
    #print("DEBUG=====================================")
    #print(request_keys[3])
    return render(request, "index.html", {"request_keys": request_keys})

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "index.html")

def sign_up(request):
    return render(request, "registration.html")

def post_sign_up(request):
    email = request.POST.get('email')
    password = request.POST.get('pass')

    try:
        user = auth.create_user(email=email, password=password)
        print("DEBUG USER CREATION---------------------------")
        print(user)
        #uid = user['localId']
        #idtoken = request.session['uid']
        #custom_token = auth.create_custom_token(uid, {"admin": True})
    except:
        return render(request, "registration.html")
    return render(request, "login.html")


def home_page(request):
    return render(request, 'index.html')
