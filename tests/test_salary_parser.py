from src.parsers.salary_parser import SalaryParser


def test_salary_parser():

    result = SalaryParser.parse(
        "55 LPA"
    )

    assert result == 5500000