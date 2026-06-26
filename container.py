from dependency_injector import containers
from dependency_injector import providers

from src.infrastructure.database.session import SessionLocal


class Container(
    containers.DeclarativeContainer
):

    db_session = providers.Singleton(
        SessionLocal
    )