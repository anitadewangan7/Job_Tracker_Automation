from datetime import datetime

from src.domain.entities.job import Job
from src.domain.entities.resume import ResumeProfile
from src.scorers.job_scorer import JobScorer


def test_job_score():

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
        target_roles=["Principal SDET"],
        preferred_locations=["Bangalore", "Remote"]
    )

    job = Job(
        job_id="1",
        title="Principal SDET",
        company="Google",
        location="Bangalore",
        source="LinkedIn",
        salary="55 LPA",
        posted_date=datetime.now(),
        description="""
        Python Playwright
        Docker Kubernetes
        API Testing
        """,
        url="url",
        collected_at=datetime.now()
    )

    score = JobScorer.score(
        job,
        resume
    )

    assert score > 80