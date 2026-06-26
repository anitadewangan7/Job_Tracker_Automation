from src.ai.matcher import AIMatcher
from src.ai.mock_provider import (
    MockAIProvider
)

from src.domain.entities.resume import (
    ResumeProfile
)


class DummyJob:

    description = (
        "Python Playwright"
    )


def test_ai_matcher():

    resume = ResumeProfile(
        skills=["Python"],
        years_experience=10,
        target_roles=["SDET"],
        preferred_locations=[
            "Remote"
        ]
    )

    matcher = AIMatcher(
        MockAIProvider()
    )

    result = matcher.match(
        resume,
        DummyJob()
    )

    assert result.match_score == 88