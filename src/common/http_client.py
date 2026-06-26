import requests

from src.common.retry import retry


class HttpClient:

    @retry(retries=3)

    def get(
        self,
        url,
        **kwargs
    ):

        response = requests.get(
            url,
            timeout=20,
            **kwargs
        )

        response.raise_for_status()

        return response