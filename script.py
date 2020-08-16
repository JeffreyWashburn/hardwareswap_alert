# Imports
from praw import Reddit

from re import compile, IGNORECASE

from smtplib import SMTP
from email.message import EmailMessage
from win10toast import ToastNotifier

from time import sleep
from datetime import datetime as dt
from traceback import format_exc

from json import load, dump
from os.path import isfile

from private.creds import my_credentials as mycreds

# Constants (Enter your search patterns here)
NOTIFY_IMG = "icons/hardwareswap.ico"
HWSWAP_NEW = "https://www.reddit.com/r/hardwareswap/new"

GRAPHICS_CARD = compile(r"2080 ?super", IGNORECASE)
IS_PAYPAL = compile(r"PayPal", IGNORECASE)
IS_USA = compile(r"^\[USA")
ALL = compile(r".*")

# Functions
def win_notify(post):
    toaster = ToastNotifier()
    toaster.show_toast(title="Found on r/hardwareswap", msg=post, 
        icon_path=NOTIFY_IMG)

def email_alert(subject, body, to):
    message = EmailMessage()
    message.set_content(f"{body}\nLink: {HWSWAP_NEW}")
    message['subject'] = subject
    # message is going to myself
    message['to'] = to
    message['from'] = to

    user = mycreds['email']
    password = mycreds['gmail_app_password']

    server = SMTP("smtp.gmail.com", 587) # 587 is standard for smtp
    server.starttls()
    server.login(user, password)

    server.send_message(message)

    server.quit()

def get_newest(sub_reddit):
    # get the three newest non-sticky posts
    return [post.title for post in sub_reddit.new(limit=3) if not 
            post.stickied and post.link_flair_text == "SELLING" or
            post.link_flair_text == "TRADING"]

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

def get_now():
    return dt.strftime(dt.now(), "%Y%m%d %H-%M-%S")

def main():
    print(f"[{get_now()}][START]: CTRL-C to quit")

    # create history file if none
    if not isfile("history.json"):
        with open("history.json", "w") as f:
            dump([], f)

    # make a hardwareswap subreddit instance
    # (your credentials go here)
    reddit = Reddit(
        client_id=mycreds['client_id'],
        client_secret=mycreds['client_secret'],
        user_agent=mycreds['user_agent']
    )

    # list to hold already discovered posts so you dont get notified every 5s
    discovered = load_discovered()
    while len(discovered) < 3:
        discovered.append(None)
        save_discovered(discovered)
    
    while True:
        # reddits api is limited to no more than 30 requests per minute (2/sec)
        sleep(5) # pause for 5 seconds to be safe
        hardwareswap = reddit.subreddit("hardwareswap")
        # check against expressions
        # customize and add more checks as necessary
        matches = check(hardwareswap, IS_USA)
        total = 0
        for post in matches:
            if post not in discovered:
                # send windows notification and sms text
                win_notify(post)
                email_alert("Found on r/hardwareswap", post, 
                    mycreds['phone_address'])
                # remember last 3 posts
                discovered.pop(0)
                discovered.append(post)
                save_discovered(discovered)
                total += 1
                print(f"[{total}][NOTIFICATION SENT]: {post}")

try:
    main()
except:
    var = format_exc()
    with open(f"err/{get_now()} traceback.err", "w") as f:
        f.write(var)