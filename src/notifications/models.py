from dataclasses import dataclass


@dataclass
class Notification:
    subject: str
    body: str