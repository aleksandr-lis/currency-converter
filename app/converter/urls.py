from django.urls import path
from .views import CurrenciesViewSet, RatesViewSet, ConvertView


urlpatterns = [
    path('currencies/', CurrenciesViewSet.as_view({'get': 'list'}), name='currencies'),
    path('rates/', RatesViewSet.as_view({'get': 'list'}), name='rates'),
    path('<str:fr>/<str:to>/<str:value>/', ConvertView.as_view({'get': 'list'}), name='convert'),
]
