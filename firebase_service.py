import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

class FirebaseService():
    def __init__(self):
        cred = credentials.Certificate("credentials.json")
        firebase_admin.initialize_app(cred)
    
    def get_user_by_email(self, email):
        user = auth.get_user_by_email(email)
        return user
    
    def list_users(self):
        all_users = auth.list_users()
        return all_users.iterate_all()

    def sign_up(self):
        email = input("write your email")
        password = input("write your password")
        auth.create_user(email=email, password=password)

    def delete_user(self, email):
        user = self.get_user_by_email(email)
        auth.delete_user(user.uid)

    def update_user_email(self, old_email, new_email):
        user = self.get_user_by_email(old_email)
        auth.update_user(user.uid, email=new_email)
        