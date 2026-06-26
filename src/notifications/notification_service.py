from src.notifications.models import Notification


class NotificationService:

    def __init__(self):

        self.notifiers = []

    def register(self, notifier):

        self.notifiers.append(notifier)

    def notify(self, notification: Notification):

        for notifier in self.notifiers:

            notifier.send(notification)