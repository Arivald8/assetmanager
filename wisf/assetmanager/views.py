from django.shortcuts import render

from firebase_admin import auth
from decouple import config as cfg

from assetmanager.authenticator import Authenticator
from assetmanager.devicedbmanager import DeviceDBManager


def sign_in(request):
    return render(request, "login.html")

def post_sign_in(request):
    validation = Authenticator().user_sign_in(request=request)
    return validation

def logout(request):
    validation = Authenticator().user_logout(request)
    return validation

def sign_up(request):
    return render(request, "registration.html")

def post_sign_up(request):
    validation = Authenticator().user_sign_up(request)  
    return render(validation[0], validation[1])


def home_page(request):
    return render(request, 'index.html')


def admin_dashboard(request):
    if Authenticator().is_admin(request):
        return render(request, "admins.html")
    else:
        return render(request, *[_ for _ in Authenticator().access_denied()])


def admin_dashboard_add_claims(request):
    if Authenticator().is_admin(request):
        validation = Authenticator().add_user_claims(request)
        return render(validation[0], validation[1], validation[2])
    else:
        return render(request, *[_ for _ in Authenticator().access_denied()])


def check_user_claims(request):
    Authenticator().check_user_claims(request)


def show_user_claims(request):
    try:
        claims = auth.verify_id_token(request.session['idToken'])
    except:
        return render(_ for _ in Authenticator().access_denied())
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
    user_claims = Authenticator().user_permissions_generic_elevated(request)
    if True in user_claims:
        return render(*DeviceDBManager().view_assets(request))
    else:
        return render(request, *[_ for _ in Authenticator().access_denied()])

def asset_manager_add_asset(request):
    if True in Authenticator().user_permissions_generic_elevated(request):
        return render(*DeviceDBManager().add_asset(request))
    else:
        return render(request, *[_ for _ in Authenticator().access_denied()])
        


        