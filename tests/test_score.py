from src.domain.entities.score import JobScore


def test_job_score():

    score = JobScore(
        match_score=95,
        skill_match_score=90,
        salary_score=100,
        location_score=100,
        ai_score=95
    )

    assert score.match_score == 95