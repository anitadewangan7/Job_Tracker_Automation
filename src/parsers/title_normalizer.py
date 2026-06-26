class TitleNormalizer:

    TARGET_TITLES = {

        "staff sdet": "Staff SDET",

        "principal sdet": "Principal SDET",

        "lead qa automation":
        "Lead QA Automation Engineer"
    }

    @classmethod
    def normalize(cls, title):

        title_lower = title.lower()

        for key, value in cls.TARGET_TITLES.items():

            if key in title_lower:
                return value

        return title