import firebase_service

fb = firebase_service.FirebaseService()

users = fb.list_users()

for user in users:
    fb.update_user_email(user.email, 'test@mail.com')