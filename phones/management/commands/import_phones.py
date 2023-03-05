import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                id, name, image, price, release_date, lte_exists, slug = line.values()
                slug = slugify(name)
                phone = Phone(id=id, name=name, image=image, price=price, release_date=release_date,
                              lte_exists=lte_exists, slug=slug)
                phone.save()
