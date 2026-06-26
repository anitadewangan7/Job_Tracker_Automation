import json

from src.domain.entities.ai_match_result import (
    AIMatchResult
)


class AIResponseParser:

    @staticmethod
    def parse(response: str):

        data = json.loads(response)

        return AIMatchResult(
            match_score=data["match_score"],
            missing_skills=data["missing_skills"],
            strengths=data["strengths"],
            interview_probability=data[
                "interview_probability"
            ]
        )