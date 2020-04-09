from twilio.rest import Client
import os
"""Here we're defining the environment variable for everything"""
title = os.getenv("INPUT_IUTITLE")
num = os.getenv("INPUT_IUNUM")
actor = os.getenv('GITHUB_ACTOR')
accountSid = os.getenv('TWILIO_ACCOUNT_SID')
atoken = os.getenv('TWILIO_AUTH_TOKEN')
event = os.getenv("GITHUB_EVENT_NAME")
repo = os.getenv("GITHUB_REPOSITORY")
state=os.getenv('INPUT_EVE_STATE')
from_num=os.getenv('INPUT_FROM_NUM')
to_num=os.getenv('INPUT_TO_NUM')
if title is None:
    title = os.getenv('INPUT_PRTITLE')
if num is None:
    num = os.getenv('INPUT_PRNUM')
# ---------- Here we want to check for the responses ---------------

if event=="pull_request":
    if state=="opened":
        response=f'A new Pull Request (#{num}) is opened in {repo} by {actor} with title: \"{title}\"'
    elif state=='closed':
        response=f'The Pull Request (#{num}) on {repo} is closed by {actor}'
elif event=='issues':
    if state=='opened':
        response=f'A new Issue (#{num}) is opened in {repo} by {actor} with title: \"{title}\"'
    elif state=='closed':
        response=f'The Issue (#{num}) on {repo} is closed by {actor}'
else:
    response=f'Unknown Event is trigerred'

# ------------ Starting the client -------------
client=Client(accountSid,atoken) 
print(response)
print('Sending Message')
message = client.messages.create(body=response,from_=from_num,to=to_num)
print('Message Sent')