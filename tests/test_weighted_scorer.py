from src.scorers.weighted_scorer import (
    WeightedScorer
)


def test_weighted_score():

    result = WeightedScorer.calculate(
        100,
        100,
        100,
        100,
        100
    )

    assert result == 100