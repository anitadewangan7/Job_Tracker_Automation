from src.collectors.career_site import (
    CareerSiteCollector
)


def test_career_site_collector():

    collector = CareerSiteCollector()

    jobs = collector.collect()

    assert len(jobs) == 1