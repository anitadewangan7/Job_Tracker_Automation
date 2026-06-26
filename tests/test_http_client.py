from unittest.mock import patch
from unittest.mock import MagicMock

from src.common.http_client import (
    HttpClient
)


@patch("requests.get")
def test_http_client(mock_get):

    response = MagicMock()

    response.raise_for_status.return_value = None

    mock_get.return_value = response

    client = HttpClient()

    result = client.get(
        "https://example.com"
    )

    assert result == response