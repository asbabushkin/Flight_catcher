import json

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from flight_search.models import CityCode


class Command(BaseCommand):

    @staticmethod
    def add_objects(model, reader):
        model_object = model
        for row in reader:
            try:
                model_object.objects.create(**row)
            except IntegrityError as e:
                print(f"Ошибка {e} при загрузке {row}")
        return f"Database Update {model}"

    def handle(self, *args, **options):
        with open("flight_search/data/cities.json", "rb") as cities:
            reader_cities = json.load(cities)
        self.stdout.write(
            self.style.SUCCESS(self.add_objects(CityCode, reader_cities))
        )