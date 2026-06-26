from abc import ABC, abstractmethod

from src.notifications.models import Notification


class Notifier(ABC):

    @abstractmethod
    def send(self, notification: Notification):
        pass