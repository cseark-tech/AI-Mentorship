import json
from storage.storage import Storage

class JsonStorage(Storage):

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
        with open(
            "data/employees.json",
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)