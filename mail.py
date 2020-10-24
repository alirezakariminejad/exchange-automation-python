import smtplib
from config import receiver_mail
from email.mime.text import MIMEText


def send_msg_smtp(subject, body):
    msg = MIMEText(body)
    msg["subject"] = subject
    msg["to"] = receiver_mail
    msg["from"] = "design@niafam.com"
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as mail_server:
        mail_server.login("519fafc3271284", "a40a4f63e858d5")
        mail_server.sendmail(msg["from"], msg["to"], msg.as_string())
