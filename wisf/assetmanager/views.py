from django.shortcuts import render
from decouple import config as cfg

from firebase_admin import auth

from assetmanager.authenticator import Authenticator


def sign_in(request):
    return render(request, "login.html")

def post_sign_in(request):
    validation = Authenticator().user_sign_in(request=request)
    return render(validation[0], validation[1], validation[2])

def logout(request):
    validation = Authenticator().user_logout(request)
    return render(validation[0], validation[1])

def sign_up(request):
    return render(request, "registration.html")

def post_sign_up(request):
    validation = Authenticator().user_sign_up(request)
    return render(validation[0], validation[1])


def home_page(request):
    return render(request, 'index.html')


def add_admin_claim(request):
    user_id = request.session['uid']
    user_obj = auth.get_user(user_id)
    print("DEBUG HERE ============================")
    print(user_id)
    print(user_obj)
    print("DEBUG STOPPPP")
    auth.set_custom_user_claims(user_id, {'admin': True})
    claims = auth.verify_id_token(request.session['idToken'])
    if claims['admin'] is True:
        print("It works")
    else:
        print("IT doesn't work")

    print("DEBUG 2 ============================")
    print(user_obj.custom_claims.get('admin'))


    return render(request, "index.html")

def show_user_claims(request):
    claims = auth.verify_id_token(request.session['idToken'])
    try:
        if claims['admin'] is True:
            print("User is an admin")
            print(auth.get_user(request.session['uid']).custom_claims.get('admin'))
        else:
            print("Not an admin")
    except KeyError:
        print("Not an admin")
    return render(request, "index.html")