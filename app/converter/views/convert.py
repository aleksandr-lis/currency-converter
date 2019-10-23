from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from converter.models import Rates
from converter.serializers import ConvertSerializer


class ConvertView(viewsets.ViewSet):
    def list(self, request, fr, to, value):
        fr = fr.lower()
        to = to.lower()

        fr_rate = Rates.objects.filter(
            curr_id=fr.upper(),
        ).order_by('-id')[:1].first()

        to_rate = Rates.objects.filter(
            curr_id=to.upper(),
        ).order_by('-id')[:1].first()

        if not fr_rate or not to_rate:
            raise APIException({
                'error': 'Wrong request',
            })

        try:
            result = to_rate.value * float(value) / fr_rate.value
        except ValueError:
            raise APIException({
                'error': 'Wrong request',
            })

        queryset = {
            'result': result,
            'code': to.upper(),
        }
        serializer = ConvertSerializer(queryset, many=False)
        return Response(serializer.data)
