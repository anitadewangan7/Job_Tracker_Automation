from sqlalchemy.orm import Session

from src.domain.entities.job import Job

from src.infrastructure.database.models import JobModel


class SqlJobRepository:

    def __init__(
        self,
        session: Session
    ):
        self.session = session

    def save(
        self,
        job: Job
    ):

        model = JobModel(
            **job.__dict__
        )

        self.session.merge(model)

       

    def get_by_job_id(
        self,
        job_id: str
    ):

        return self.session.get(
            JobModel,
            job_id
        )

    def get_all(self):

        return self.session.query(
            JobModel
        ).all()