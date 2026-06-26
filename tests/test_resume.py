from src.domain.entities.resume import ResumeProfile


def test_resume_profile():

    profile = ResumeProfile(
        skills=["Python", "Playwright"],
        years_experience=10,
        target_roles=["Principal SDET"],
        preferred_locations=["Bangalore"]
    )

    assert profile.years_experience == 10