import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth



class FirebaseService():
    def __init__(self):
        cred = credentials.Certificate("credentials.json")
        firebase_admin.initialize_app(cred)

    def sign_up(self):
        email = input("write your email")
        password = input("write your password")
        auth.create_user(email=email, password=password)

    def delete_user(self,email):
        user = auth.get_user_by_email(email)
        auth.delete_user(user.uid)





