from src.collectors.linkedin import (
    LinkedInCollector
)


def test_linkedin_collector():

    collector = LinkedInCollector()

    jobs = collector.collect()

    assert len(jobs) == 2