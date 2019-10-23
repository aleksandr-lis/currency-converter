from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Currencies, Rates
from .serializers import CurrenciesSerializer, RatesSerializer, ConvertSerializer


class ViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_currency(code, name):
        Currencies.objects.create(
            code=code,
            name=name,
        )

    @staticmethod
    def create_rates(base, curr, value):
        Rates.objects.create(
            base_id=base,
            curr_id=curr,
            value=value,
        )

    def setUp(self):
        self.create_currency('ABC', 'Alfabet Currency')
        self.create_currency('XYZ', 'Math Currency')
        self.create_rates('ABC', 'ABC', 1)
        self.create_rates('ABC', 'XYZ', 0.15)


class GetAllCurrenciesTest(ViewTest):

    def test_get_all_currencies(self):
        response = self.client.get(
            reverse('currencies')
        )
        expected = Currencies.objects.all().order_by('code')
        serialized = CurrenciesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)


class GetAllRatesTest(ViewTest):

    def test_get_all_rates(self):
        response = self.client.get(
            reverse('rates')
        )
        expected = Rates.objects.all().order_by('curr_id')
        serialized = RatesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)


class ConvertTest(ViewTest):

    def test_convert(self):
        response = self.client.get(
            reverse('convert', kwargs={
                'fr': 'ABC',
                'to': 'xyz',
                'value': '10',
            })
        )
        expected = {
            'result': '1.5',
            'code': 'XYZ',
        }
        serialized = ConvertSerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
