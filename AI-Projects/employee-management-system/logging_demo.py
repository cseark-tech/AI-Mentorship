import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


try:
    number = int("ABC")

except ValueError:
    logging.error("Failed to convert value to integer")