import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Debug message")
logging.info("Employee added successfully")
logging.warning("Employee salary is unusually high")
logging.error("Employee not found")
logging.critical("Application failure")