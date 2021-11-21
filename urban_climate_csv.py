import csv
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


class DataSource:
    def read(self, **kwargs):
        temperatures_by_hour = {}
        with open(Path(BASE_DIR).joinpath(kwargs['file_name']), 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                hour = datetime.strptime(row[0], '%d/%m/%Y %H:%M').isoformat()
                temperature = float(row[2])
                temperatures_by_hour[hour] = temperature
        return temperatures_by_hour
