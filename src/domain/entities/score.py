from dataclasses import dataclass


@dataclass
class JobScore:

    match_score: float

    skill_match_score: float

    salary_score: float

    location_score: float

    ai_score: float