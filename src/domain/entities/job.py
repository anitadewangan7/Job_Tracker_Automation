from dataclasses import dataclass
from datetime import datetime


@dataclass
class Job:

    job_id: str
    title: str
    company: str
    location: str
    source: str
    salary: str | None
    posted_date: datetime
    description: str
    url: str
    collected_at: datetime