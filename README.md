# r/hardwareswap post monitor

## To use:

### Install script dependencies
* pip install win10toast
* pip install praw

### Set up your gmail to send texts :email:
1. Go to your gmail's [security settings]("https://myaccount.google.com/security") and enable two-factor authentication
1. On the same page, you should now see an app passwords section. Go in there and create a new app and get a password for it. You will use this password in the script.
1. Use your carriers [phone number address](https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/) in place of an email address to instead get sms text messages.

### Authenticate with reddits API
I recommend doing what I did with creating a creds.py file to hold all your keys and stuff so that it's secure, otherwise there are a [few ways](https://praw.readthedocs.io/en/latest/getting_started/configuration.html#configuration) to authenticate other than hard coding your credentials like the below example.
```python
# hard coded reddit api credentials
hardwareswap = reddit.subreddit(
    client_id="YOUR CLIENT ID HERE",
    client_secret="YOUR CLIENT SECRET HERE",
    user_agent="YOUR USER AGENT HERE"
)
```
1. Go to your [apps](https://reddit.com/prefs/apps) on the reddit site and add a new app.
1. Give it a name.
1. Select script.
1. Enter a redirect URI. I chose https://127.0.0.1
1. The string at the top under 'personal use script' and underneath your name is your `client_id`. Your `client_secret` is also displayed. Note these down somewhere secure.
1. Create a descriptive `user_agent`. Reddit requires these to identify applications. An example: `my_app_name v1.0.0 by /u/my_name`
1. Make sure your three credential strings get into the script either by hardcoding them in (see above example) or by storing them in a seperate file (recommended).

### Common errors
* Recieved HTTP response `401` - This most likely means your credentials are wrong :thinking:

# PRAW (Python Reddit API Wrapper)
`praw` is the main package used in this script. It is a wrapper written in Python for Reddit's API, as the name suggests.
Take a look at the [documentation](https://praw.readthedocs.io/en/latest/) to figure out how you can further customize this script and make it your own :smiley:
