from src.collectors.linkedin import LinkedInCollector
from src.collectors.career_site import CareerSiteCollector


class CollectorRegistry:

    _collectors = {

        "linkedin": LinkedInCollector,

        "career_site": CareerSiteCollector
    }

    @classmethod
    def get(cls, name):

        collector = cls._collectors.get(name)

        if not collector:

            raise ValueError(
                f"Unknown collector {name}"
            )

        return collector()