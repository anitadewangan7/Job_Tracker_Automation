import time


class RateLimiter:

    def __init__(self, calls_per_second=1):

        self.calls_per_second = calls_per_second

        self.last_call = 0

    def wait(self):

        current = time.time()

        elapsed = current - self.last_call

        minimum_interval = 1 / self.calls_per_second

        if elapsed < minimum_interval:

            time.sleep(
                minimum_interval - elapsed
            )

        self.last_call = time.time()