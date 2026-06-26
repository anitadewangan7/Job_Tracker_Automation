from src.application.collector_service import CollectorService


def main():

    service = CollectorService()

    jobs = service.collect_jobs()

    for job in jobs:
        print(f"{job.company:<20} {job.title}")


if __name__ == "__main__":
    main()