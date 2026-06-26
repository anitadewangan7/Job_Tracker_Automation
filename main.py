from src.infrastructure.database.models import Base

from src.infrastructure.database.session import engine


def startup():

    Base.metadata.create_all(
        bind=engine
    )


if __name__ == "__main__":

    startup()

    print("Application Started")