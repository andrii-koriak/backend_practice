import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth



class FirebaseService():
    def init_app():
        cred = credentials.Certificate("credentials.json")
        firebase_admin.initialize_app(cred)

    def sign_up(): 
        email = input("write your email")
        password = input("write your password")
        auth.create_user(email=email, password=password)
