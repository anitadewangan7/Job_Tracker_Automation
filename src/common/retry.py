import time
import functools


def retry(
    retries: int = 3,
    delay: int = 2
):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            last_exception = None

            for attempt in range(retries):

                try:
                    return func(*args, **kwargs)

                except Exception as ex:

                    last_exception = ex

                    time.sleep(delay)

            raise last_exception

        return wrapper

    return decorator