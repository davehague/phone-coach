import os
from twilio.rest import Client

def make_call(to_number, speech_content):
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml=f"<Response><Say>{speech_content}</Say></Response>",
        to=to_number,
        from_="+15017122661",  # Replace with your Twilio number
    )
    return call.sid
