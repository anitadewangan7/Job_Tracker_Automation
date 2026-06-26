from datetime import datetime

from src.domain.entities.job import Job

from src.infrastructure.database.session import SessionLocal

from src.infrastructure.database.repositories.job_repository import (
    SqlJobRepository
)


def test_save_job():

    session = SessionLocal()

    repo = SqlJobRepository(
        session
    )

    job = Job(
        job_id="1",
        title="Principal SDET",
        company="Google",
        location="Bangalore",
        source="LinkedIn",
        salary="50LPA",
        posted_date=datetime.now(),
        description="",
        url="https://job",
        collected_at=datetime.now()
    )

    repo.save(job)

    result = repo.get_by_job_id("1")

    assert result.company == "Google"