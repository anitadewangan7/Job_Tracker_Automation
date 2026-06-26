from datetime import datetime

from src.domain.entities.job import Job
from src.filters.duplicate_filter import DuplicateFilter


def test_duplicate_filter():

    job1 = Job(
        job_id="1",
        title="Principal SDET",
        company="Google",
        location="Bangalore",
        source="LinkedIn",
        salary="55 LPA",
        posted_date=datetime.now(),
        description="Python",
        url="u1",
        collected_at=datetime.now()
    )

    job2 = Job(
        job_id="2",
        title="Principal SDET",
        company="Google",
        location="Remote",
        source="Naukri",
        salary="60 LPA",
        posted_date=datetime.now(),
        description="Python",
        url="u2",
        collected_at=datetime.now()
    )

    result = DuplicateFilter.remove_duplicates(
        [job1, job2]
    )

    assert len(result) == 1