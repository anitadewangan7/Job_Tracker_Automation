from src.ai.matcher import AIMatcher
from src.ai.mock_provider import (
    MockAIProvider
)

from src.application.collector_service import (
    CollectorService
)

from src.domain.entities.resume import (
    ResumeProfile
)

resume = ResumeProfile(
    skills=[
        "Python",
        "Playwright",
        "Docker",
        "Kubernetes",
        "API"
    ],
    years_experience=10,
    target_roles=[
        "Principal SDET"
    ],
    preferred_locations=[
        "Bangalore",
        "Remote"
    ]
)

service = CollectorService()

jobs = service.collect_jobs()

matcher = AIMatcher(
    MockAIProvider()
)

for job in jobs:

    result = matcher.match(
        resume,
        job
    )

    print(
        f"\n{job.company}"
    )

    print(
        f"Match Score: "
        f"{result.match_score}"
    )

    print(
        f"Strengths: "
        f"{result.strengths}"
    )

    print(
        f"Missing Skills: "
        f"{result.missing_skills}"
    )