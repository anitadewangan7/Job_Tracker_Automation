
from src.infrastructure.database.unit_of_work import UnitOfWork


def test_uow():

    with UnitOfWork() as uow:

        assert uow.session is not None