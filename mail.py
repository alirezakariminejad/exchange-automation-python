import smtplib
from config import receive_mail

from email.mime.text import MIMEText

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("519fafc3271284", "a40a4f63e858d5")
    server.sendmail(sender, receiver, message)
