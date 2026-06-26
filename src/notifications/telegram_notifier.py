import os
import requests

from src.notifications.base import Notifier
from src.notifications.models import Notification


class TelegramNotifier(Notifier):

    def send(self, notification: Notification):

        token = os.getenv("TELEGRAM_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")

        requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": notification.body
            },
            timeout=30
        )