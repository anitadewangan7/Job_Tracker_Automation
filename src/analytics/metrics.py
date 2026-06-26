class Metrics:

    @staticmethod
    def average_score(results):

        if not results:
            return 0

        return round(
            sum(r["score"] for r in results)
            / len(results),
            2
        )

    @staticmethod
    def company_distribution(results):

        distribution = {}

        for item in results:

            company = item["company"]

            distribution[company] = (
                distribution.get(company, 0) + 1
            )

        return distribution