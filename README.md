# r/hardwareswap post monitor

## To use:

### Install dependencies
* pip install win10toast
* pip install praw

### Get your credentials
I reccommend doing what I did with creating a creds.py file to hold all your keys and stuff so that it's secure, otherwise there are a [few ways](https://praw.readthedocs.io/en/latest/getting_started/configuration.html#configuration) to authenticate other than hard coding your credentials like the below example.

```python
# hard coded reddit api credentials
hardwareswap = reddit.subreddit(
    client_id="YOUR CLIENT ID HERE",
    client_secret="YOUR CLIENT SECRET HERE",
    user_agent="YOUR USER AGENT HERE"
)
```

### Set up your gmail to send texts
1. Go to your gmail's [security settings]("https://myaccount.google.com/security") and enable two-factor authentication
1. On the same page, you should now see an app passwords section. Go in there and create a new app and get a password for it. You will use this password in the script.
1. Use your carriers [phone number address](https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/) in place of an email address to instead get sms text messages.

### Authenticate with reddits API
* Make sure your three credential strings get into the script either by hardcoding them in (above) or by storing them in a seperate file (recommended).

* To get these go to your [apps](https://reddit.com/prefs/apps) on the reddit site and add an app.

### Common errors
* Recieved error `401` - This most likely means your credentials are wrong :thinking:

# PRAW (Python Reddit API Wrapper)
`praw` is the main package used in this script. It is a wrapper written in Python for Reddit's API, as the name suggests.
Take a look at the [documentation](https://praw.readthedocs.io/en/latest/) to figure out how you can further customize this script and make it your own :smiley: