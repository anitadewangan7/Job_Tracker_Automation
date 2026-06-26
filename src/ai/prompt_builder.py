from src.domain.entities.resume import ResumeProfile


class PromptBuilder:

    @staticmethod
    def build(
        resume: ResumeProfile,
        job_description: str
    ) -> str:

        return f"""
You are a Senior Technical Recruiter.

Candidate Skills:
{", ".join(resume.skills)}

Experience:
{resume.years_experience} years

Target Roles:
{", ".join(resume.target_roles)}

Job Description:
{job_description}

Return ONLY JSON:

{{
  "match_score": 0-100,
  "missing_skills": [],
  "strengths": [],
  "interview_probability": "Low|Medium|High"
}}
"""