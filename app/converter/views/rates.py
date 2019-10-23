from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from converter.models import Rates
from converter.serializers import RatesSerializer


class RatesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Rates.objects.raw('''
            select * from converter_rates where id in (
                select max(id) from converter_rates group by curr_id
            ) order by curr_id;
        ''')
        serializer = RatesSerializer(queryset, many=True)
        return Response(serializer.data)
