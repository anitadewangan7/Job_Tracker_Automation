import os
import smtplib

from email.mime.text import MIMEText

from src.notifications.base import Notifier
from src.notifications.models import Notification
from src.infrastructure.config.settings import settings


class EmailNotifier(Notifier):

    def send(self, notification: Notification):

        # sender = os.getenv("EMAIL_ADDRESS")
        # password = os.getenv("EMAIL_PASSWORD")
        # receiver = os.getenv("EMAIL_TO")

        sender = settings.email_address
        password = settings.email_password
        receiver = settings.email_to

        print(f"Sender: {sender}")
        print(f"Receiver: {receiver}")
        print(f"Password is None? {password is None}")

        msg = MIMEText(notification.body)

        msg["Subject"] = notification.subject
        msg["From"] = sender
        msg["To"] = receiver

        with smtplib.SMTP("smtp.gmail.com", 587) as server:

            server.starttls()

            server.login(sender, password)

            server.send_message(msg)