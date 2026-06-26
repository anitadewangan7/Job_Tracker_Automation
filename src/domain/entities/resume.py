from dataclasses import dataclass


@dataclass
class ResumeProfile:

    skills: list[str]

    years_experience: int

    target_roles: list[str]

    preferred_locations: list[str]