import json
import logging
from storage.storage import Storage

class JsonStorage(Storage):
    logger = logging.getLogger(__name__)

    def save(self, employees):
        data = []
        for employee in employees:
            data.append(employee.to_dict())

        with open(
            "data/employees.json",
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
            with open("data/employees.json", "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            self.logger.exception(
                "Failed to parse employee JSON data"
            )
            raise