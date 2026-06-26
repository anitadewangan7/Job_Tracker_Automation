import json

from src.ai.base import AIProvider


class MockAIProvider(AIProvider):

    def generate(
        self,
        prompt: str
    ) -> str:

        return json.dumps(
            {
                "match_score": 88,
                "missing_skills": [
                    "Grafana"
                ],
                "strengths": [
                    "Python",
                    "Playwright"
                ],
                "interview_probability":
                    "High"
            }
        )