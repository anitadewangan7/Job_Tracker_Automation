import pandas as pd


class CSVReport:

    @staticmethod
    def generate(
        data,
        output_file="jobs.csv"
    ):

        df = pd.DataFrame(data)

        df.to_csv(
            output_file,
            index=False
        )

        return output_file