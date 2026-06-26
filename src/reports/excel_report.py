import pandas as pd


class ExcelReport:

    @staticmethod
    def generate(
        data,
        output_file="jobs.xlsx"
    ):

        df = pd.DataFrame(data)

        df.to_excel(
            output_file,
            index=False
        )

        return output_file