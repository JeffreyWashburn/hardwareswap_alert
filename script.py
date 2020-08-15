# Imports
import praw
import re
import smtplib
from email.message import EmailMessage
from win10toast import ToastNotifier
from time import sleep

# bring in my private credentials
from private.creds import *

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
    message.set_content(body)
    message['subject'] = subject
    message['to'] = to
    message['from'] = to

    user = email[0]
    password = email[1]

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)

    server.send_message(message)

    server.quit()

def get_newest(sub_reddit):
    return [post.title for post in sub_reddit.new() if not post.
    stickied]

def matches(list, keyword):

    # check any list for keywords
    found = []
    for item in list:
        if keyword.search(item):
            found.append(item)
    return found

def check(subreddit, keyword):

    # check a subreddits posts for keywords
    found = []
    for post in get_newest(subreddit):
        if keyword.search(post):
            found.append(post)
    return found

def main():
    
    # make a hardwareswap subreddit instance
    # (your credentials go here)
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

    hardwareswap = reddit.subreddit("hardwareswap")

    # list to hold already discovered posts so you dont get notified every 5s
    discovered = []
    while True:
        sleep(5)
        # check against expressions
        # customize and add more checks as necessary
        pass_1 = check(hardwareswap, PATTERN1)
        for i in range(len(pass_1)):
            post = pass_1[i]
            if post not in discovered:
                win_notify(post)
                email_alert("Found on r/hardwareswap", post, phoneno)
                sleep(2)
                discovered.append(post)

main()