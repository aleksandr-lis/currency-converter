from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from converter.models import Currencies
from converter.serializers import CurrenciesSerializer


class CurrenciesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Currencies.objects.all().order_by('code')
        serializer = CurrenciesSerializer(queryset, many=True)
        return Response(serializer.data)
