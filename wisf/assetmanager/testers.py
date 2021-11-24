import firebase_admin
from firebase_admin import auth
from decouple import config as cfg

default_app = firebase_admin.initialize_app(firebase_admin.credentials.Certificate(f"{cfg('GOOGLE_CREDENTIALS')}")), 
        

auth.set_custom_user_claims('bFXHKJlmsAZya0CaNSarQo4731F3',{'admin': True, 'test_claim': True})