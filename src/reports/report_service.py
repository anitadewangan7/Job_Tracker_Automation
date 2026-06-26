from src.reports.csv_report import CSVReport
from src.reports.excel_report import ExcelReport
from src.reports.html_report import HTMLReport


class ReportService:

    @staticmethod
    def generate_all(data):

        CSVReport.generate(data)

        ExcelReport.generate(data)

        HTMLReport.generate(data)