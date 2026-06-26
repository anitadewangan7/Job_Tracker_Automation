import re


class SkillExtractor:

    KNOWN_SKILLS = {
        "python",
        "selenium",
        "playwright",
        "pytest",
        "docker",
        "kubernetes",
        "api",
        "rest",
        "github actions",
        "jenkins",
        "grafana",
        "prometheus",
        "observability",
        "ai testing",
        "automation",
    }

    @classmethod
    def extract(cls, text: str) -> set[str]:

        text = text.lower()

        found = set()

        for skill in cls.KNOWN_SKILLS:

            if re.search(re.escape(skill), text):
                found.add(skill)

        return found