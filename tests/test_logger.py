from src.common.logger import logger


def test_logger():

    logger.info(
        "test_log",
        service="job_tracker"
    )

    assert True