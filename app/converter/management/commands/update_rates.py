import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from converter.models import Currencies, Rates


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Get data

        curr_all = [c.code for c in Currencies.objects.all()]
        response = requests.get(
            'https://openexchangerates.org/api/latest.json', params={
                'app_id': settings.OER_APP_ID,
                'base': settings.OER_BASE,
                'symbols': ','.join(curr_all),
            }).json()

        # Save data

        for curr, value in response['rates'].items():
            print('{}, {} = {:f}'.format(
                response['base'], curr, value,
            ))
            Rates.objects.create(
                base_id=response['base'],
                curr_id=curr,
                value=value,
            )
