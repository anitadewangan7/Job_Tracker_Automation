from src.parsers.title_normalizer import (
    TitleNormalizer
)


def test_title_normalizer():

    result = (
        TitleNormalizer.normalize(
            "Senior Principal SDET"
        )
    )

    assert result == "Principal SDET"