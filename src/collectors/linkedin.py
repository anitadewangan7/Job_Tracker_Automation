from datetime import datetime

from src.collectors.base import JobCollector
from src.domain.entities.job import Job


class LinkedInCollector(JobCollector):

    def collect(self):

        return [

            Job(
                job_id="LI001",
                title="Principal SDET",
                company="Google",
                location="Bangalore",
                source="LinkedIn",
                salary="55 LPA",
                posted_date=datetime.now(),
                description="Python Playwright",
                url="https://linkedin.com/job1",
                collected_at=datetime.now()
            ),

            Job(
                job_id="LI002",
                title="Staff SDET",
                company="Atlassian",
                location="Remote",
                source="LinkedIn",
                salary="60 LPA",
                posted_date=datetime.now(),
                description="Python Kubernetes",
                url="https://linkedin.com/job2",
                collected_at=datetime.now()
            )
        ]