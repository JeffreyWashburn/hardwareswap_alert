# Imports
import praw
import re
import smtplib
from email.message import EmailMessage
from win10toast import ToastNotifier
from time import sleep
from json import load, dump
from os.path import isfile

# bring in my private credentials
from private.creds import *

# create history file if none
if not isfile("history.json"):
    with open("history.json", "w") as f:
        dump([], f)

# Constants (Enter your search patterns here)
NOTIFY_IMG = "icons/hardwareswap.ico"
PATTERN1 = re.compile(r"2080 ?super", re.IGNORECASE)
IS_PAYPAL = re.compile(r"PayPal", re.IGNORECASE)
IS_USA = re.compile(r"^\[USA")

# Functions
def win_notify(post):
    toaster = ToastNotifier()
    toaster.show_toast(title="Found on r/hardwareswap", msg=post, 
        icon_path=NOTIFY_IMG)

def email_alert(subject, body, to):
    message = EmailMessage()
    message.set_content(f"{body}\nLink: https://www.reddit.com/r/hardwareswap/")
    message['subject'] = subject
    # message is going to myself
    message['to'] = to
    message['from'] = to

    user = email[0]
    password = email[1]

    server = smtplib.SMTP("smtp.gmail.com", 587) # 587 is standard for smtp
    server.starttls()
    server.login(user, password)

    server.send_message(message)

    server.quit()

def get_newest(sub_reddit):
    return [post.title for post in sub_reddit.new(limit=3) if not post.
    stickied]

def check(subreddit, keyword):

    # check a subreddits posts for keywords
    found = []
    for post in get_newest(subreddit):
        if keyword.search(post):
            found.append(post)
    return found

def save_discovered(posts):
    with open("history.json", "w") as f:
        dump(posts, f)

def load_discovered():
    with open("history.json", "r") as f:
        return load(f)

def main():
    
    # make a hardwareswap subreddit instance
    # (your credentials go here)
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

    # list to hold already discovered posts so you dont get notified every 5s
    discovered = load_discovered()
    
    while True:
        sleep(1)
        hardwareswap = reddit.subreddit("hardwareswap")
        # check against expressions
        # customize and add more checks as necessary
        matches = check(hardwareswap, PATTERN1)
        for post in matches:
            if post not in discovered:
                # send windows notification and sms text
                win_notify(post)
                email_alert("Found on r/hardwareswap", post, phoneno)
                # remember last 3 posts
                print(f"removing{discovered.pop(0)}")
                discovered.append(post)
                save_discovered(discovered)
                print(f"saving {post}")
            
main()