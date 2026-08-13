import logging

def configure_logging():
    logging.getLogger(__name__).info("Application started")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )