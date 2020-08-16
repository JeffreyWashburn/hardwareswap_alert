from win10toast import ToastNotifier
from email.message import EmailMessage
from smtplib import SMTP
from hws_utils import NOTIFY_IMG, HWSWAP_NEW
from private.creds import my_credentials as mycreds

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