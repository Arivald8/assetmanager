from django.shortcuts import render
from django.core.paginator import Paginator

from firebase_admin import auth
from decouple import config as cfg

from assetmanager.authenticator import Authenticator
import assetmanager.models as models


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
    if Authenticator().is_admin(request):
        return render(request, "admins.html")
    else:
        return render(request, *[_ for _ in Authenticator().access_denied()])


def post_admin_dashboard(request):
    validation = Authenticator().add_user_claims(request)
    return render(validation[0], validation[1], validation[2])


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
        all_assets = models.Asset.objects.all()
        paginator = Paginator(all_assets, 20)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'asset_manager.html', {'page_obj': page_obj})
    else:
        return render(request, *[_ for _ in Authenticator().access_denied()])

        