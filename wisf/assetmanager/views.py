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


def admin_dashboard(request):
    try:
        claims = auth.verify_id_token(request.session['idToken'])
    except:
        return render(request, "index.html", {'unauthorized': "Access Denied"})
    try:
        if claims['admin'] is True:
            return render(request, "admins.html")
        else:
            return render(request, "index.html", {'unauthorized': "Access Denied"})
    except KeyError:
        return render(request, "index.html", {'unauthorized': "Access Denied"})

def post_admin_dashboard(request):
    validation = Authenticator().add_user_claims(request)
    return render(validation[0], validation[1], validation[2])


def show_user_claims(request):
    claims = auth.verify_id_token(request.session['idToken'])
    try:
        if claims['admin'] is True:
            print(auth.get_user(request.session['uid']).custom_claims.get('admin'))
            print(request.session['uid'])
        else:
            print("Not an admin")
    except KeyError:
        print("Not an admin")
    return render(request, "index.html")

def asset_manager(request):
    claims = auth.verify_id_token(request.session['idToken'])
    try:
        if claims['admin'] is True:
            # allow in

            pass
        else:
            return render(request, "index.html", {'unauthorized': "Access Denied"})
    except:
        return render(request, "index.html", {'unauthorized': "Access Denied"})

        