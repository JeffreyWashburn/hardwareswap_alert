# r/hardwareswap post monitor
## To use:
### Install dependencies
* pip install win10toast
* pip install praw
### Get your credentials
I recommend doing what I did with creating a creds.py file to hold all your keys and stuff so that it's secured, otherwise you can hardcode them into the script yourself, just replace the values in the script.
### Set up your gmail to send texts
1. Go to your gmail's [security settings](https://myaccount.google.com/security) and enable two-factor authentication.
1. On the same page, you should now see an app passwords section. Go in there and create a new app and get a password for it. You will use this password in the script.
1. Look at [this article](https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/) to get your "phone number email", use this in place of an email address to instead get sms text messages.
### Authenticate with reddits API
* Paste your client_id, client_secret, and user_agent strings into creds.py (these will then be imported and used to instantate the reddit object in the script).
* To get these go to your [apps](https://reddit.com/prefs/apps) on the reddit site and add an app.
### Common errors
* recieved err 401 - This most likely means your credentials are wrong.
---
<br><br><br>
# PRAW (Python Reddit API Wrapper)
Take a look at the [documentation](https://praw.readthedocs.io/en/latest/) to figure out how you can further customize this script
