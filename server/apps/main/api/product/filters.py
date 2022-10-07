import django_filters
from django_filters import rest_framework as filters

from server.apps.main.models import Product


class ProductFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    price_gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ('name',)
