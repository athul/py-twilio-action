from twilio.rest import Client
import os
"""Here we're defining the environment variable for everything"""
title = os.getenv("INPUT_IUTITLE")
num = os.getenv("INPUT_IUNUM")
actor = os.getenv('GITHUB_ACTOR')
event = os.getenv("GITHUB_EVENT_NAME")
repo = os.getenv("GITHUB_REPOSITORY")
action = os.getenv('INPUT_EVENT_ACTION')
from_num = os.getenv('INPUT_FROM_NUM')
to_num = os.getenv('INPUT_TO_NUM')
if title is None:
    title = os.getenv('INPUT_PRTITLE')
if num is None:
    num = os.getenv('INPUT_PRNUM')
# ---------- Here we want to check for the responses ---------------
if event == "pull_request":
    github_url = f'https://github.com/{repo}/pulls/{num}'
    if action == "opened":
        response = f'A new Pull Request (#{num}) is opened in {repo} by {actor} with title: \"{title}\" URL: {github_url}'
    elif action == 'closed':
        response = f'The Pull Request (#{num}) on {repo} is closed by {actor}, URL: {github_url}'
elif event == 'issues':
    github_url = f'https://github.com/{repo}/issues/{num}'
    if action == 'opened':
        response = f'A new Issue (#{num}) is opened in {repo} by {actor} with title: \"{title}\" URL: {github_url}'
    elif action == 'closed':
        response = f'The Issue (#{num}) on {repo} is closed by {actor}, URL: {github_url}'
else:
    github_url = f'https://github.com/{repo}'
    response = f'A new {event} has occured in the {repo} by {actor},URL: {github_url}'

# ------------ Starting the client -------------
client = Client()
print(response)
print('Sending Message')
message = client.messages.create(body=response, from_=from_num, to=to_num)
print('Message Sent')
