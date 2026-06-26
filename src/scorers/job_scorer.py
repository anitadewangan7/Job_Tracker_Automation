from src.domain.entities.resume import ResumeProfile

from src.parsers.skill_extractor import SkillExtractor
from src.parsers.salary_parser import SalaryParser
from src.scorers.weighted_scorer import WeightedScorer


class JobScorer:

    @classmethod
    def score(
        cls,
        job,
        resume_profile: ResumeProfile

    ):

        title_score = (
            100
            if "sdet" in job.title.lower()
            else 50
        )

        job_skills = SkillExtractor.extract(
            job.description
        )

        target_skills = {
            skill.lower()
            for skill in resume_profile.skills
        }

        overlap = len(
            target_skills.intersection(
                job_skills
            )
        )

        skill_score = (
            overlap /
            len(target_skills)
        ) * 100

        salary = SalaryParser.parse(
            job.salary
        )

        salary_score = (
            100
            if salary >= 3000000
            else 50
        )

        location_score = (
            100
            if job.location.lower()
            in [loc.lower() for loc in resume_profile.preferred_locations]
            else 50
        )

        freshness_score = 100

      

        return round(
            WeightedScorer.calculate(
                title_score,
                skill_score,
                salary_score,
                location_score,
                freshness_score
            ),
            2
        )