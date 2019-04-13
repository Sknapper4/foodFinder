import django_filters
from .models import Snack, Store


class SnackFilter(django_filters.FilterSet):

    class Meta:
        model = Snack
        fields = {
            'name': ['icontains']
        }

        def my_snack_filter(self, queryset, snack, value):
            return queryset.filter(**{
                snack: value,
            })
