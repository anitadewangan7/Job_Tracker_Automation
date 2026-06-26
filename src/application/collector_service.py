from src.collectors.factory import (
    CollectorFactory
)


class CollectorService:

    def collect_jobs(self):

        jobs = []

        for source in [
            "linkedin",
            "career_site"
        ]:

            collector = (
                CollectorFactory.create(
                    source
                )
            )

            jobs.extend(
                collector.collect()
            )

        return jobs