from src.parsers.skill_extractor import SkillExtractor


def test_skill_extraction():

    description = """
    Python Playwright Docker Kubernetes
    """

    skills = SkillExtractor.extract(description)

    assert "python" in skills
    assert "playwright" in skills
    assert "docker" in skills