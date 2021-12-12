import assetmanager.models as models
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import JsonResponse

class DeviceDBManager:
    def __init__(self):
        pass


    def view_assets(self, request):
        print("hello from view_assets")
        return JsonResponse({
            'page_obj': Paginator(
                models.Asset.objects.all(), 20).get_page(request.GET.get('page'))
        })


    def add_asset(self, request):
        try:
            models.Asset.objects.create(
                device_pk = request.POST.get("device_pk"),
                device_name = request.POST.get('device_name'),
                device_type = request.POST.get('device_asset'),
                device_serial = request.POST.get('device_serial'),
                device_model = request.POST.get('device_model'),
                device_location = request.POST.get('device_location'),
                device_ip = request.POST.get('device_ip'),
                device_mac = request.POST.get('device_mac'),
                device_school = request.POST.get('device_school'),
                device_notes = request.POST.get('device_notes')
            )
            return [
                request, 
                "asset_manager.html", 
                {"message": "Success! Asset has been added to the database."}
            ]
        except (ValidationError, IntegrityError):
            return [
                request, 
                "asset_manager.html", 
                {"message": "Some of the filds have incorrect values. Please try again."}
            ]
    
    def add_asset_form_data(self, request):
        return {
            "device_pk": request.POST.get("device_pk"),
            "device_name": request.POST.get('device_name'),
            "device_type": request.POST.get('device_asset'),
            "device_serial": request.POST.get('device_serial'),
            "device_model": request.POST.get('device_model'),
            "device_location": request.POST.get('device_location'),
            "device_ip": request.POST.get('device_ip'),
            "device_mac": request.POST.get('device_mac'),
            "device_school": request.POST.get('device_school'),
            "device_notes": request.POST.get('device_notes')
        }
