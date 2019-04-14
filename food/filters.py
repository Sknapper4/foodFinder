import django_filters
from .models import Snack, Store


class StoreFilter(django_filters.FilterSet):

    class Meta:
        model = Store
        fields = {
            'city': ['icontains'],
        }

        def my_store_filter(self, queryset, city, value):
            return queryset.filter(**{
                city: value,
            })


class SnackFilter(django_filters.FilterSet):

    class Meta:
        model = Snack
        fields = {
            'name': ['icontains'],
        }

        def my_snack_filter(self, queryset, snack, value):
            return queryset.filter(**{
                snack: value,
            })


