from twilio.rest import Client
from utils.config import Config

account_sid = Config.TwilioAccountSid
auth_token = Config.TwilioAuthToken
service_sid = Config.TwilioServiceSid

client = Client(account_sid, auth_token)

def send_otp(phone_number):
    try:
        verification = client.verify.services(service_sid).verifications.create(to=phone_number, channel='sms')
        return verification.status
    except Exception as e:
        print(f'Error: {e}')
        return False

def verify_otp(phone_number, otp):
    try:
        verification_check = client.verify.services(service_sid).verification_checks.create(to=phone_number, code=otp)
        return verification_check.status == 'approved'
    except Exception as e:
        print(f'Error: {e}')
        return False
