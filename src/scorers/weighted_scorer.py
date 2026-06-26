class WeightedScorer:

    WEIGHTS = {

        "title": 30,

        "skills": 40,

        "salary": 10,

        "location": 10,

        "freshness": 10
    }

    @classmethod
    def calculate(
        cls,
        title_score,
        skill_score,
        salary_score,
        location_score,
        freshness_score
    ):

        return (

            title_score * 0.30 +

            skill_score * 0.40 +

            salary_score * 0.10 +

            location_score * 0.10 +

            freshness_score * 0.10
        )