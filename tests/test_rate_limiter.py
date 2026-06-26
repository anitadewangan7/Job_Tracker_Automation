from src.common.rate_limiter import (
    RateLimiter
)


def test_rate_limiter():

    limiter = RateLimiter(
        calls_per_second=100
    )

    limiter.wait()

    assert True