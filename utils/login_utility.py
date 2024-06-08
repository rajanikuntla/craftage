from firebase_admin import auth
from firebase_admin.auth import UserNotFoundError


def get_user_token(phone_number):
    try:
        user = auth.get_user_by_phone_number(phone_number=phone_number)
        return auth.create_custom_token(user.uid)
    except UserNotFoundError :
        user = auth.create_user(phone_number=phone_number)
        return auth.create_custom_token(user.uid)
    

def verify_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token['uid']
    except Exception as e:
        return 'Invalid token'