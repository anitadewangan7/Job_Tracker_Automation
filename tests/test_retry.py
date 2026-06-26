from src.common.retry import retry

counter = {"count": 0}


@retry(retries=3, delay=0)
def flaky():

    counter["count"] += 1

    if counter["count"] < 3:
        raise Exception()

    return True


def test_retry():

    assert flaky() is True