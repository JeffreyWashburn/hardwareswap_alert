# r/hardwareswap post monitor
## To use:
### Install dependencies
* pip install win10toast
* pip install praw
### Authenticate with reddits API
* Paste your client_id, client_secret, and user_agent strings into creds.py (these will then be imported and used to instantate the reddit object in the script)
* To get these go to your [apps](https://reddit.com/prefs/apps) on the reddit site and add an app
### Common errors
* recieved err 401 - This most likely means your credentials are wrong