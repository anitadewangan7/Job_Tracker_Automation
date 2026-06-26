from scripts.collect_jobs import main as collect_jobs
from scripts.score_jobs import main as score_jobs
from scripts.generate_report import main as generate_report
from scripts.send_notifications import main as send_notifications
from src.common.logger import logger


def main():
    logger.info("=" * 60)
    logger.info("Job Intelligence Platform")
    logger.info("=" * 60)

    logger.info("Collecting jobs...")
    collect_jobs()


    logger.info("Scoring jobs...")
    score_jobs()
    logger.info("Scoring completed.")


    logger.info("Generating reports...")
    generate_report()
    logger.info("Reports generated.")


    logger.info("Sending notifications...")
    send_notifications()
    logger.info("Notifications sent.")

    logger.info("Pipeline completed successfully.")


if __name__ == "__main__":
    main()