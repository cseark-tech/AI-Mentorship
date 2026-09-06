import json
import logging
from storage.storage import Storage

class JsonStorage(Storage):
    logger = logging.getLogger(__name__)

    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, employees):
        data = []
        for employee in employees:
            data.append(employee.to_dict())

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                data,
                file,
                indent=4
            )

    def load(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            self.logger.exception(
                "Failed to parse employee JSON data"
            )
            raise