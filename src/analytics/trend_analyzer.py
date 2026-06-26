import matplotlib.pyplot as plt


class TrendAnalyzer:

    @staticmethod
    def company_chart(
        distribution,
        output_file="companies.png"
    ):

        companies = list(
            distribution.keys()
        )

        counts = list(
            distribution.values()
        )

        plt.figure()

        plt.bar(
            companies,
            counts
        )

        plt.tight_layout()

        plt.savefig(
            output_file
        )

        plt.close()

        return output_file