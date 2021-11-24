from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from assetmanager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name="home"),
    path('signin/', views.sign_in),
    path('postsignin/', views.post_sign_in),
    path('signup/', views.sign_up, name="signup"),
    path('logout/', views.logout, name="log"),
    path('postsignup/', views.post_sign_up),
    #path('customclaim/', views.add_admin_claim),
    path('showclaims/', views.show_user_claims),
    path('admindash/', views.admin_dashboard),
    path('addclaims/', views.admin_dashboard_add_claims),
    path('manager/', views.asset_manager),
]
