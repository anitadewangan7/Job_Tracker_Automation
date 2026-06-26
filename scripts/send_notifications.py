from src.notifications.email_notifier import EmailNotifier
from src.notifications.telegram_notifier import TelegramNotifier
from src.notifications.notification_service import NotificationService
from src.notifications.models import Notification
from src.notifications.templates import JobTemplate

from dotenv import load_dotenv

load_dotenv()

def main():
    rows = [
        {
            "company": "Google",
            "title": "Principal SDET",
            "score": 92,
            "url": "https://careers.google.com"
        },
        {
            "company": "Atlassian",
            "title": "Staff SDET",
            "score": 90,
            "url": "https://www.atlassian.com/careers"
        }
    ]

    notification = Notification(
        subject="Daily QA/SDET Jobs",
        body=JobTemplate.top_jobs(rows)
    )


    service = NotificationService()

    # Enable the channels you want
    service.register(EmailNotifier())
    service.register(TelegramNotifier())

    service.notify(notification)

    print("Notifications sent.")

if __name__ == "__main__":
    main()

