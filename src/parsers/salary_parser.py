import re


class SalaryParser:

    @staticmethod
    def parse(salary: str) -> int:

        if not salary:
            return 0

        match = re.search(r"(\d+)", salary)

        if not match:
            return 0

        lpa = int(match.group(1))

        return lpa * 100000