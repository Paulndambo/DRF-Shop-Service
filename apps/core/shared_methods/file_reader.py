import csv
import json


class FileReaderMixin:
    def __init__(self, file) -> None:
        self.file = file

    def read_csv_file(self):
        try:
            data = []
            with open(self.file, "r") as f:
                data = list(csv.DictReader(f))

            return data
        except Exception as e:
            raise e

    def read_json_file(self):

        try:
            data = []

            with open(self.file, "r") as f:
                data = json.load(f)

            return data

        except Exception as e:
            raise e

    def read_excel_file(self):
        pass
