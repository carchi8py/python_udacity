from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC2b3bc3f123bc228561be2e1076a9a596"
auth_token  = "ea8c7639c45500a0414130999d5ffbc4"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="My name is Ron Burgandy?",
    to="+16505045125",    # Replace with your phone number
    from_="+16505130388") # Replace with your Twilio number
print message.sid