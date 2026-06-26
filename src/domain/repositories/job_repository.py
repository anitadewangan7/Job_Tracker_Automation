from abc import ABC
from abc import abstractmethod

from domain.entities.job import Job


class JobRepository(ABC):

    @abstractmethod
    def save(self, job: Job):
        pass

    @abstractmethod
    def get_by_job_id(self, job_id: str):
        pass

    @abstractmethod
    def get_all(self):
        pass