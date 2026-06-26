from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class JobModel(Base):

    __tablename__ = "jobs"

    job_id = Column(
        String,
        primary_key=True
    )

    title = Column(String)

    company = Column(String)

    location = Column(String)

    source = Column(String)

    salary = Column(String)

    posted_date = Column(DateTime)

    description = Column(String)

    url = Column(String)

    collected_at = Column(DateTime)