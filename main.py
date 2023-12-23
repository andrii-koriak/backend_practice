import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

email = input("write your email")
password = input("write your password")

user = auth.create_user(email=email, password=password)
