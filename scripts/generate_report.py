from src.application.collector_service import (
    CollectorService
)

from src.domain.entities.resume import (
    ResumeProfile
)

from src.scorers.job_scorer import (
    JobScorer
)

from src.analytics.metrics import (
    Metrics
)

from src.analytics.trend_analyzer import (
    TrendAnalyzer
)

from src.reports.report_service import (
    ReportService
)

def main():

    resume = ResumeProfile(
        skills=[
            "Python",
            "Playwright",
            "Docker",
            "Kubernetes",
            "API"
        ],
        years_experience=10,
        target_roles=["Principal SDET"],
        preferred_locations=[
            "Bangalore",
            "Remote"
        ]
    )

    jobs = (
        CollectorService()
        .collect_jobs()
    )

    report_rows = []

    for job in jobs:

        score = (
            JobScorer.score(
                job,
                resume
            )
        )

        report_rows.append(
            {
                "company": job.company,
                "title": job.title,
                "location": job.location,
                "salary": job.salary,
                "score": score,
                "url": job.url,
                "source": job.source
            }
        )

    ReportService.generate_all(
        report_rows
    )

    distribution = (
        Metrics.company_distribution(
            report_rows
        )
    )

    TrendAnalyzer.company_chart(
        distribution
    )

print("Reports generated")

if __name__ == "__main__":
    main()