from src.application.collector_service import (
    CollectorService
)

from src.infrastructure.database.unit_of_work import (
    UnitOfWork
)

from src.infrastructure.database.repositories.job_repository import (
    SqlJobRepository
)

service = CollectorService()

jobs = service.collect_jobs()

with UnitOfWork() as uow:

    repo = SqlJobRepository(
        uow.session
    )

    for job in jobs:

        repo.save(job)

print(
    f"Saved {len(jobs)} jobs"
)