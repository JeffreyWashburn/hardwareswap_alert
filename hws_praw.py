from praw import Reddit
from hws_utils import load_discovered, save_discovered
from hws_notifications import win_notify, email_alert
from time import sleep
from private.creds import my_credentials as mycreds

def get_newest(sub_reddit, flair_filters):
    # get the three newest non-sticky posts

    found = []
    for post in sub_reddit.new(limit=3):
        if not post.stickied:
            for filter in flair_filters:
                if not post.link_flair_text == filter.upper():
                    found.append(post.title)
    return found


def check(subreddit, patterns, flair_filters):

    # check a subreddits posts for keywords
    # TODO: Check subreddits posts agains a list of patterns

    found = []
    for pattern in patterns:
        for post in get_newest(subreddit, flair_filters):
            if pattern.search(post):
                found.append(post)
    return found

def authenticate(credentials):
    reddit = Reddit(
        client_id=credentials['client_id'],
        client_secret=credentials['client_secret'],
        user_agent=credentials['user_agent']
    )
    return reddit

def monitor(patterns, flair_filters):

    # list to hold discovered posts to prevent duplicate notifications
    discovered = load_discovered()
    
    total = 0
    while True:
        # pause every 5s so we dont overload reddits api
        sleep(5)
        # instantiate subreddit and check for patterns
        hardwareswap = authenticate(mycreds).subreddit("hardwareswap")
        # check() function actually makes the api calls
        matches = check(hardwareswap, patterns, flair_filters)
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