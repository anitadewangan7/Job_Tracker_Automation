# tests/test_repository.py

from datetime import datetime

from src.domain.entities.job import Job
from src.infrastructure.database.session import SessionLocal
from src.infrastructure.database.repositories.job_repository import SqlJobRepository


def test_save_job():

    session = SessionLocal()

    repo = SqlJobRepository(session)

    job = Job(
        job_id="TEST001",
        title="Staff SDET",
        company="Atlassian",
        location="Remote",
        source="LinkedIn",
        salary="60 LPA",
        posted_date=datetime.now(),
        description="Playwright Python",
        url="https://example.com",
        collected_at=datetime.now()
    )

    repo.save(job)

    result = repo.get_by_job_id("TEST001")

    assert result.company == "Atlassian"