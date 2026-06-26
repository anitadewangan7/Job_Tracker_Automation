import logging
import structlog


def configure_logging():

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(
                fmt="iso"
            ),
            structlog.processors.JSONRenderer()
        ]
    )

    logging.basicConfig(
        level=logging.INFO
    )


logger = structlog.get_logger()