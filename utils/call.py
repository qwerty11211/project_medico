# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACd827012c9f6a29f44dce6654edfa6da8"
auth_token = "55d06c238d460gd9768217824b171dde"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="It is send to take your medicine- Benazepril. 2 doses in the morning. ",
    from_="+18507893715",
    to="+91913805225"
)

response = VoiceResponse()
s = 'Hey, this is from Medico. This is reminder to take your medicine- Benazepril. 2 doses in the morning.  '
response.say(s, voice='alice')
response.record(timeout=10, transcribe=True)
call = client.calls.create(
    twiml=response,
    from_='+18507893715',
    to='+91913805225'
)
print(call.sid)
