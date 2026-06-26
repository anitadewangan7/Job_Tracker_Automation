from abc import ABC
from abc import abstractmethod

from src.domain.entities.job import Job


class JobCollector(ABC):

    @abstractmethod
    def collect(self) -> list[Job]:
        """
        Returns normalized jobs
        """
        pass