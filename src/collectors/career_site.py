from datetime import datetime

from src.collectors.base import JobCollector
from src.domain.entities.job import Job


class CareerSiteCollector(JobCollector):

    def collect(self):

        return [

            Job(
                job_id="CS001",
                title="Lead QA Automation",
                company="BrowserStack",
                location="Remote",
                source="CareerSite",
                salary="40 LPA",
                posted_date=datetime.now(),
                description="Playwright API",
                url="https://browserstack.com/job",
                collected_at=datetime.now()
            )
        ]