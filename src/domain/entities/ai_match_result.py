from dataclasses import dataclass


@dataclass
class AIMatchResult:

    match_score: int

    missing_skills: list[str]

    strengths: list[str]

    interview_probability: str