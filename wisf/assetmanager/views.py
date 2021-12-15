from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Asset
from .serializers import AssetSerializer
from .pagination import CustomPagination

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


@api_view(['GET', 'POST'])
def asset_manager(request):
    user_claims = Authenticator().user_permissions_generic_elevated(request)
    if True in user_claims:
        if request.method == 'GET':
            assets = Asset.objects.all()
            serializer = AssetSerializer(assets, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = AssetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return render(request, *[_ for _ in Authenticator().access_denied()])

def asset_manager_add_asset(request):
    if True in Authenticator().user_permissions_generic_elevated(request):
        return render(*DeviceDBManager().add_asset(request))
    else:
        return render(request, *[_ for _ in Authenticator().access_denied()])
        

class ListAssets(GenericAPIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Asset
            fields = [
                'device_name',
                'device_type',
                'device_asset',
                'device_serial',
                'device_model',
                'device_location',
                'device_ip',
                'device_mac',
                'device_school',
                'device_notes',
            ]
    def get(self, request):
        asset_qs = Asset.objects.all().order_by('-id')
        page = self.paginate_queryset(asset_qs)
        if page is not None:
            serializer = self.OutputSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        # If page is not specified, return all
        serializer = self.OutputSerializer(asset_qs, many=True)
        return Response(serializer.data)
        