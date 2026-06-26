from src.application.collector_service import (
    CollectorService
)

from src.domain.entities.resume import (
    ResumeProfile
)

from src.scorers.job_scorer import (
    JobScorer
)

def main():
    resume = ResumeProfile(
        skills=[
            "Python",
            "Playwright",
            "Selenium",
            "Docker",
            "Kubernetes",
            "Pytest",
            "API"
        ],
        years_experience=10,
        target_roles=[
            "Principal SDET",
            "Staff SDET",
            "Lead QA Automation Engineer"
        ],
        preferred_locations=[
            "Bangalore",
            "Remote"
        ]
    )

    service = CollectorService()

    jobs = service.collect_jobs()

    scored = []

    for job in jobs:

        score = JobScorer.score(
            job,
            resume
        )

        scored.append(
            (score, job)
        )

    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )

    for score, job in scored:

        print(
            f"{job.company:15}"
            f" Score={score}"
        )


if __name__ == "__main__":
    main()