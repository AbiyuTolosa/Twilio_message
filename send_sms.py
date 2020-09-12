from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio

client = TwilioRestClient(account_sid, auth_token)

my_msg = "Abiyu's message"

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)